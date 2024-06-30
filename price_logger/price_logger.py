from abc import ABC, abstractmethod 

class PriceLogger(ABC):
    '''Parent abstract class in charge of the structure behind processing raw fetched prices 
    and logging them to a destination'''

    @abstractmethod
    def configure_logger(config):
        '''Configure parameters for the logger'''
        pass
    
    @abstractmethod
    def open_logger(self):
        '''Connect to the destination to log data'''
        pass

    @abstractmethod
    def log_input(self, price1, price2):
        '''Log the price with a specific format to a destination'''
        pass

    @abstractmethod
    def close_logger(self):
        '''Close connections to the destination'''
        pass

    @abstractmethod
    def get_type(self):
        '''Get the type of the specific PriceLogger'''
        pass