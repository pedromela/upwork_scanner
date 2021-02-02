"""
Profile settings spider module
"""
from scrapy.selector import Selector
from spiders.base_spider import BaseSpider
from items.profile import Profile

class UpworkProfileSettingsSpider(BaseSpider):
    """
    Profile settings spider module
    """
    name = 'UpworkProfileSettingsSpider'
    allowed_domains = ['toscrape.com']

    def __init__(self, upwork_controller):
        super().__init__(upwork_controller)

    def parse(self, response):
        """
        Overrides scrapy parse function
        """
        page_source = self.upwork_controller.get_source_profile_settings()

        # Hand-off between Selenium and Scrapy happens here
        sel = Selector(text=page_source)
        # Extract data
        xpath = "//input[@data-test='firstNameEdit']"
        first_name = self.upwork_controller.get_input_value_by_xpath(xpath)
        xpath = "//input[@data-test='lastNameEdit']"
        last_name = self.upwork_controller.get_input_value_by_xpath(xpath)
        full_name = str(first_name) + " " + str(last_name)
        email = self.upwork_controller.get_input_value_by_xpath("//input[@data-test='emailEdit']")
        picture_url = sel.xpath("//div[@aria-label='Account Settings']/img/@src").get()
        phone_number = sel.xpath("//div[@data-test='phone']/text()").get()
        line1 = sel.xpath("//span[@data-test='addressStreet']/text()").get()
        line2 = sel.xpath("//span[@data-test='addressStreet2']/text()").get()
        city = sel.xpath("//span[@data-test='addressCity']/text()").get()
        state = sel.xpath("//span[@data-test='addressState']/text()").get()
        postal_code = sel.xpath("//span[@data-test='addressZip']/text()").get()
        country = sel.xpath("//span[@data-test='addressCountry']/text()").get()

        profile = Profile(first_name=first_name,
                          last_name=last_name,
                          full_name=full_name,
                          email=email,
                          picture_url=picture_url,
                          phone_number=phone_number.strip(),
                          address={
                            'line1':line1,
                            'line2':line2,
                            'city':city,
                            'state':state,
                            'postal_code':postal_code,
                            'country':country
                              }
                          )
        profile.serialize()
        yield profile.dict()
