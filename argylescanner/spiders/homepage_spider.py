"""
Home spider module
"""
from scrapy.selector import Selector
from spiders.base_spider import BaseSpider
from items.job import Job

class UpworkHomeSpider(BaseSpider):
    """
    Home spider class
    """
    name = 'UpworkHomeSpider'
    allowed_domains = ['toscrape.com']
    upwork_controller = None

    def __init__(self, upwork_controller):
        super().__init__(upwork_controller)

    def parse(self, response):
        page_source = self.upwork_controller.get_source_home()

        # Hand-off between Selenium and Scrapy happens here
        if page_source =='ERROR':
            return 'ERROR'
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
            job.serialize()
            yield job.dict()
