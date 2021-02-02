"""
UpworkController module
"""
from driver import Driver

class UpworkController(Driver):
    """
    UpworkController class
    """
    URL = 'https://www.upwork.com/'
    LOGIN_URL = 'https://www.upwork.com/ab/account-security/login'
    HOME_URL = 'https://www.upwork.com/ab/find-work/domestic'
    CONTACTINFO_URL = 'https://www.upwork.com/freelancers/settings/contactInfo'
    USERNAME = 'bob-veryhardwork'
    PASSWORD = 'Argyleawesome123!'
    SECRET_ANSWER='Bobworker'

    def __init__(self):
        super().__init__()
        self.init()

    def __del__(self):
        self.browser.quit()

    def init(self):
        """
        Init method
        """
        self.browser.get(self.URL) # go to upwork.com like a normal person would do

        if '/login' in self.browser.current_url:
            self.login()
        if self.browser.current_url == self.URL:
            self.click_home_login()
            self.login()

    def click_home_login(self):
        """
        Click login button when url = www.upwork.com
        """
        self.click_button_by_xpath("//span[contains(text(), 'Log In')]")

    def check_and_goto_page_url(self, url):
        """
        If url not equal to arg url go to arg url,
        if not logged in, log in and go to arg url
        """
        if url not in self.browser.current_url:
            self.browser.get(url)
        if self.is_logged_in() is False:
            self.login()
            if url not in self.browser.current_url:
                self.browser.get(url)

    def is_logged_in(self):
        """
        Check if user is currently logged in
        """
        element = self.try_get_element_by_xpath("//div[@aria-label='Account Settings']/img")
        if element is not None:
            return True
        return False

    def login(self):
        """
        Login method
        """
        try:
            if '/login' not in self.browser.current_url:
                self.browser.get(self.LOGIN_URL)
            self.prepare_input_by_id('login_username', self.USERNAME)
            self.click_button_by_id('login_password_continue')
            self.wait_for_field_visibility_by_id('login_password')
            self.prepare_input_by_id('login_password', self.PASSWORD)
            self.click_button_by_id('login_control_continue')

            self.wait_for_field_visibility_xpath("//section[contains(@class, 'job-tile')]")
            return True
        except Exception:
            return False

    def get_source_home(self):
        """
        go to HOME_URL and get source code
        """
        try:
            self.check_and_goto_page_url(self.HOME_URL)

            page_source = self.browser.page_source
        except Exception:
            page_source = 'ERROR'

        return page_source

    def get_source_profile_settings(self):
        """
        go to CONTACTINFO_URL and get source code
        """
        page_source = self.go_to_profile_settings()

        return page_source

    def go_to_profile_settings(self):
        """
        go to CONTACTINFO_URL and get source code
        """
        try:
            self.check_and_goto_page_url(self.HOME_URL)

            self.wait_for_field_visibility_xpath("//div[@aria-label='Account Settings']/img")
            self.click_button_by_xpath("//div[@aria-label='Account Settings']/img")
            self.click_button_by_xpath("//a[@href='/freelancers/settings/contactInfo']")
            self.browser.implicitly_wait(1)

            if self.CONTACTINFO_URL not in self.browser.current_url:
                device_auth = self.try_get_element_by_xpath("//h1[contains(text(),'Device authorization')]")
                if device_auth is not None:
                    self.prepare_input_by_name('deviceAuth[answer]', self.SECRET_ANSWER)
                    self.click_button_by_xpath("//button[@button-role='save']")
                    self.browser.implicitly_wait(1)
                    if self.CONTACTINFO_URL not in self.browser.current_url:
                        reenterpassword_header = self.try_get_element_by_xpath("//h1[contains(text(),'Re-enter password')]")
                        if reenterpassword_header is not None:
                            self.prepare_input_by_name('sensitiveZone[password]', self.PASSWORD)
                            self.click_button_by_xpath("//button[@button-role='continue']")

            self.click_button_by_xpath("//h2[contains(text(),'Account')]/preceding-sibling::button")
            self.wait_for_field_visibility_xpath("//input[@data-test='firstNameEdit']")

            page_source = self.browser.page_source
        except Exception:
            page_source = 'ERROR'
        return page_source
