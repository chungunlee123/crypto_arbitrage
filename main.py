import importlib
import json

from price_getter.api_caller_upbit import APICallerUpBit
from price_getter.web_crawler_satoshi import WebCrawlerSatoshi
from price_logger.file_logger import FileLogger

def load_config_file():
    with open("config.json", "r") as file:
        config = json.load(file)

    return config

def main():
    # Load Config File
    configuration = load_config_file()

    # Create caller instances
    price_getters = []
    for key in configuration:
        getter_config = configuration[key]
        module = importlib.import_module("price_getter")
        class_ = getattr(module, key.lower())
        instance = getattr(class_, getter_config["Class"])()
        price_getters.append(instance)

    # Configure price getter instances
    for price_getter, key in zip(price_getters, configuration):
        price_getter.configure(configuration[key])

    # Call get prices on instances and process the raw data
    # also dispose the getters once used.
    processed_data = []
    for price_getter in price_getters:
        data = price_getter.parse_raw(price_getter.get_price())
        processed_data.append(data)
        price_getter.dispose()

    # Open and configure logger
    logger = FileLogger()
    logger.configure_logger({})
    logger.open_logger()

    # Log each combination of pairs
    for i, pd in enumerate(processed_data):
        rest = processed_data[i + 1:]

        # Iterate over the other data to create unique pairs to compare
        for r in rest:
            logger.log_input(pd, r)

    # Close logger 
    logger.close_logger()

if __name__ == "__main__":
    price_getters = []
    error_flags = 0
    while error_flags != 10:
        try:
            main()
        except Exception as error:
            error_flags += 1
            print(error)
        finally:
            # In case of shutdown dispose all instances of getters
            for price_getter in price_getters:
                price_getter.dispose()