from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from datetime import datetime

import time
import re

from .price_getter import PriceGetter

class WebCrawlerSatoshi(PriceGetter):
    '''Class that performs WebScraping to get a certain crypto_symbol'''

    def configure(self, config):
        '''Configure parameters for the WebCrawler'''
        self.platform = config["Platform"]
        self.driverPath = config["WebDriverPath"]
        self.url = config["URL"]
        self.targetXPath = config["TargetXPath"]

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-ssl-errors=yes')
        self.options.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Remote(
                command_executor=self.driverPath,
                options=self.options
            )

    def get_price(self):
        '''Function that gets a crypto_symbol as input and performs a fetch
        based on the programs configuration file'''
        self.driver.get(self.url)
        time.sleep(10)
        return self.driver.find_element(By.XPATH, self.targetXPath)

    def parse_raw(self, response):
        '''Retrieve the price from the raw data and return a dictionary with the format:
        {"platform": <Platform Name>, "timestamp": <Now>,  "price": <Retrieved Price>}'''
        price = float(re.sub("[A-Z ]", "", response.text.replace(',', '')))

        return {
            "platform": self.platform,
            "timestamp": datetime.now(),
            "price": price
        }

    def dispose(self):
        '''Close and dispose the webcrawler'''
        #close the browser
        self.driver.close()
        self.driver.quit()

        # Dispose driver
        self.driver = None

    def get_type(self):
        '''Get the type of getter i.e., WebCrawler'''
        return self.__class__.__name__
