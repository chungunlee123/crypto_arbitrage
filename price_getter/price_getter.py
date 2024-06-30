from abc import ABC, abstractmethod 

class PriceGetter(ABC):
    '''Parent class that implemented by concrete getters'''

    @abstractmethod
    def configure(self, config):
        '''Configure parameters for the getter'''
        pass

    @abstractmethod
    def get_price(self):
        '''Connect to external source and retrieve price'''
        pass

    @abstractmethod
    def parse_raw(self, input_text):
        '''Retrieve the price from the raw data and return a dictionary with the format:
        {"platform": <Platform Name>, "timestamp": <Now>,  "price": <Retrieved Price>}'''
        pass

    @abstractmethod
    def dispose(self):
        '''Dispose the getter. This includes closing connections, resetting state, etc.'''
        pass

    @abstractmethod
    def get_type(self):
        '''Get the type of the specific PriceGetter'''
        pass
