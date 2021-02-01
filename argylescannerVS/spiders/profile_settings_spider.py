import scrapy
from scrapy.selector import Selector
from upwork_controller import UpworkController
from items.profile import Profile
from items.job import Job

class UpworkProfileSettingsSpider(scrapy.Spider):
    name = 'UpworkProfileSettingsSpider'
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
        page_source = self.upwork_controller.get_source_profile_settings()
        #file = open('profile_settings.html', 'r')
        #file_text = file.read()

        # Hand-off between Selenium and Scrapy happens here
        sel = Selector(text=page_source)
        # Extract data
        first_name = self.upwork_controller.get_input_value_by_xpath("//input[@data-test='firstNameEdit']")
        last_name = self.upwork_controller.get_input_value_by_xpath("//input[@data-test='lastNameEdit']")
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
                          line1=line1,
                          line2=line2, 
                          city=city, 
                          state=state, 
                          postal_code=postal_code, 
                          country=country)
        yield profile.dict()
        #yield {
        #        'id' : '',
        #        'account' : '',
        #        'employer' : '',
        #        'created_at' : '',
        #        'updated_at' : '',
        #        'first_name' : first_name.get(),
        #        'last_name' : last_name.get(),
        #        'full_name' : email.get(),
        #        'email' : email.get(),
        #        'phone_number' : phone_number.get(),
        #        'birth_date' : '',
        #        'picture_url' : picture_url.get(),
        #        'address' : {
        #                'line1' : line1.get(),
        #                'line2' : line2.get(),
        #                'city' : city.get(),
        #                'state': state.get(),
        #                'postal_code' : postal_code.get(),
        #                'country' : country.get()
        #            },
        #        'employment_status' : '',
        #        'employment_type' : '',
        #        'job_title': '',
        #        'ssn': '',
        #        'platform_user_id' : '',
        #        'hire_dates' : [
        #                ''
        #            ],
        #        'terminations' : [{
        #                'date' : '',
        #                'reason' : ''
        #            }],
        #        'marital_status' : ''
        #    }

