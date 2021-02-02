"""
Base spider module
"""
import time
import scrapy
from upwork_controller import UpworkController

class BaseSpider(scrapy.Spider):
    """
    Base spider class
    """
    upwork_controller = None

    def __init__(self, upwork_controller):
        super().__init__()
        if upwork_controller is None:
            self.upwork_controller = UpworkController()
        else:
            self.upwork_controller = upwork_controller

    def start_requests(self):
        url = "http://quotes.toscrape.com"
        yield scrapy.Request(url=url, callback=self.parse)
