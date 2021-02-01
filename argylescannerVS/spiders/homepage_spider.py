import scrapy
from scrapy.selector import Selector
from upwork_controller import UpworkController
from items.profile import Profile
from items.job import Job

class UpworkHomeSpider(scrapy.Spider):
    name = 'UpworkHomeSpider'
    allowed_domains = ['toscrape.com'] 
    upwork_controller = None

    def __init__(self, upwork_controller):
        if(upwork_controller == None):
            self.upwork_controller = UpworkController()
        else:
            self.upwork_controller = upwork_controller

    def start_requests(self):
        url = "http://quotes.toscrape.com"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page_source = self.upwork_controller.get_source_home()
        #file = open('spiders/homepage.html', mode='r')
        #page_source = file.read()
        # Hand-off between Selenium and Scrapy happens here
        sel = Selector(text=page_source)
        # Extract data
        sections = sel.xpath("//section/div")

        for section in sections:
            selector = Selector(text=section.get())
            jobtitle = selector.xpath("//div/div/div/h4/a/text()")
            jobdescription = selector.xpath("//div/div/div/div/div/div/div/span/span/text()")
            hourlypay = selector.xpath("//div/div/div/div/small/span/strong/text()")
            proposals = selector.xpath("//div/div/div/div/div/span/small/strong/text()")
            country = selector.xpath("//div/div/div/div/small/span/span/span/span/strong[@class='text-muted client-location ng-binding']/text()")

            job = Job(jobtitle=jobtitle.get(),
                        jobdescription=jobdescription.get(),
                        hourlypay=hourlypay.get(),
                        proposals=proposals.get(),
                        country=country.get())
            
            yield job.dict()