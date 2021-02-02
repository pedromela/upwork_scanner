"""
Driver module
"""
import os
import time
import random

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

class Driver:
    """
    Driver class
    """
    DELAY = 20
    browser = None

    def __init__(self):
        self.browser = self.__prepare_browser()

    def __delay(self):
        """
        Random delay to help preventing detection
        """
        time.sleep(random.uniform(0.2,5.5))

    def __prepare_options(self):
        """
        Prepare browser options with arguments to help preventing automation detection
        """
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("user-data-dir=argyleisawesome")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        return options

    def __prepare_browser(self):
        """
        Prepare browser with options to help preventing automation detection
        """
        options = self.__prepare_options()
        cwd = os.getcwd()
        driver_path = cwd + './chromedriver_win32_hacked/chromedriver.exe'
        browser = webdriver.Chrome(options=options, executable_path=driver_path)
        user_agent = {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'}
        browser.execute_cdp_cmd('Network.setUserAgentOverride', user_agent)
        return browser

    def wait_for_field_by_id(self, element_id):
        """
        Wait for html element by element_id selection
        """
        delay = self.DELAY # seconds
        try:
            print("Waiting "+element_id)
            wait_element = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.ID, element_id)))
            return wait_element
        except TimeoutException:
            print("Field loading took too much time!")

    def wait_for_field_by_name(self, name):
        """
        Wait for html element by name selection
        """
        delay = self.DELAY # seconds
        try:
            print("Waiting "+name)
            wait_element = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.NAME, name)))
            return wait_element
        except TimeoutException:
            print("Field loading took too much time!")

    def wait_for_field_by_xpath(self, xpath):
        """
        Wait for html element by xpath selection
        """
        delay = self.DELAY # seconds
        try:
            print("Waiting "+xpath)
            wait_element = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return wait_element
        except TimeoutException:
            print("Field loading took too much time!")

    def wait_for_field_visibility_by_id(self, element_id):
        """
        Wait for html element visibility by element_id selection
        """
        delay = self.DELAY # seconds
        try:
            print("Waiting visibility "+element_id)
            wait_element = WebDriverWait(self.browser, delay).until(EC.visibility_of_element_located((By.ID, element_id)))
            return wait_element
        except TimeoutException:
            print("Field loading took too much time!")

    def wait_for_field_visibility_by_name(self, name):
        """
        Wait for html element visibility by name selection
        """
        delay = self.DELAY # seconds
        try:
            print("Waiting visibility "+name)
            wait_element = WebDriverWait(self.browser, delay).until(EC.visibility_of_element_located((By.NAME, name)))
            return wait_element
        except TimeoutException:
            print("Field loading took too much time!")

    def wait_for_field_visibility_xpath(self, xpath):
        """
        Wait for html element visibility by xpath selection
        """
        delay = self.DELAY # seconds
        try:
            print("Waiting visibility "+xpath)
            wait_element = WebDriverWait(self.browser, delay).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return wait_element
        except TimeoutException:
            print("Field loading took too much time!")

    def prepare_input_by_id(self, element_id, newvalue):
        """
        Find input by element_id and send keys
        """
        element = self.wait_for_field_by_id(element_id)
        self.__delay()
        element.send_keys(newvalue)

    def prepare_input_by_name(self, name, newvalue):
        """
        Find input by name and send keys
        """
        element = self.wait_for_field_by_name(name)
        self.__delay()
        element.send_keys(newvalue)

    def prepare_input_by_xpath(self, xpath, newvalue):
        """
        Find input by xpath and send keys
        """
        element = self.wait_for_field_by_xpath(xpath)
        self.__delay()
        element.send_keys(newvalue)

    def click_button_by_id(self, element_id):
        """
        Click button by element_id
        """
        button = self.wait_for_field_by_id(element_id)
        self.__delay()
        button.click()

    def click_button_by_name(self, name):
        """
        Click button by name
        """
        button = self.wait_for_field_by_name(name)
        self.__delay()
        button.click()

    def click_button_by_xpath(self, xpath):
        """
        Click button by xpath
        """
        button = self.wait_for_field_by_xpath(xpath)
        self.__delay()
        button.click()

    def try_get_element_by_name(self, name):
        """
        Try to find element by name
        """
        try:
            element = self.wait_for_field_by_name(name)
            return element
        except NoSuchElementException:
            return None

    def try_get_element_by_id(self, element_id):
        """
        Try to find element by element_id
        """
        try:
            element = self.wait_for_field_by_id(element_id)
            return element
        except NoSuchElementException:
            return None

    def try_get_element_by_xpath(self, xpath):
        """
        Try to find element by xpath
        """
        try:
            element = self.wait_for_field_by_xpath(xpath)
            return element
        except NoSuchElementException:
            return None

    def get_input_value_by_id(self, element_id):
        """
        Get input value by element_id
        """
        element = self.try_get_element_by_id(element_id)
        value = element.get_attribute('value')
        return value

    def get_input_value_by_name(self, name):
        """
        Get input value by name
        """
        element = self.try_get_element_by_name(name)
        value = element.get_attribute('value')
        return value

    def get_input_value_by_xpath(self, xpath):
        """
        Get input value by xpath
        """
        element = self.try_get_element_by_xpath(xpath)
        value = element.get_attribute('value')
        return value
