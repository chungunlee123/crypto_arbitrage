from .price_getter import PriceGetter
from datetime import datetime

import requests
import uuid
import jwt

class APICallerUpBit(PriceGetter):
    '''Class that performs API Calls to get a certain crypto_symbol'''

    def __init__(self):
        super().__init__()
        pass

    def configure(self, config):
        '''Configure parameters for the APICaller'''
        self.url = config["URL"]
        self.platform = config["Platform"]
        self.access_key = config["APIKey"]
        self.secret_key = config["APISecret"]

    def get_price(self):
        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
        }

        jwt_token = jwt.encode(payload, self.secret_key)
        authorization = 'Bearer {}'.format(jwt_token)
        headers = {
        'Authorization': authorization,
        }

        try:
            # Make a GET request to the Binance API
            response = requests.get(self.url, headers=headers)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                # Return raw data
                return data
            else:
                print(f"Failed to retrieve data from UpBit API. Status code: {response.status_code}")

            # Return raw response
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
        return 10

    def parse_raw(self, response):
        '''Retrieve the price from the raw data'''
        price = response[0]["trade_price"]
        return {
            "platform": self.platform,
            "timestamp": datetime.now(),
            "price": price
        }

    def dispose(self):
        '''Dispose the API Caller'''
        pass

    def get_type(self):
        '''Get the type of getter i.e., APICaller'''
        return self.__class__.__name__