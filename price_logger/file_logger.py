from .price_logger import PriceLogger
import os.path

class FileLogger(PriceLogger):
    '''Concrete class in charge of logging prices to a file'''
    
    def configure_logger(self, config):
        '''Configure parameters for the logger'''
        self.header = "Timestamp, Platform1, Price1, Platform2, Price2, Difference \n"
        self.file_name = "output.csv"

        file_exists = os.path.isfile(self.file_name)

        if not file_exists:
            with open(self.file_name, 'a') as file:
                file.write(self.header)
    
    def open_logger(self):
        '''Connect to the file'''
        self.file = open(self.file_name, 'a')

    def log_input(self, data1, data2):
        '''Log the price with a specific format to a destination'''
        # Unpack dictionary 1
        paltform1 =  data1["platform"]
        price1 = data1["price"]
        t1 = data1["timestamp"]

        # Unpack dictionary 2
        paltform2 =  data2["platform"]
        price2 = data2["price"]
        t2 = data2["timestamp"]

        # Calculated fields
        average_timestamp = t1 + (t2 - t1) / 2
        difference = price1 - price2

        # Write to file
        self.file.write("{}, {}, {}, {}, {}, {} \n".format(
            average_timestamp,
            paltform1,
            price1,
            paltform2,
            price2,
            difference
        ))

    def close_logger(self):
        '''Close connections to the file'''
        self.file.close()

    def get_type(self):
        '''Get the type of the specific PriceLogger'''
        pass