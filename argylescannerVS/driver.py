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
    DELAY = 20
    browser = None

    def __init__(self):
        self.browser = self.prepare_browser()

    def set_browser(browser):
        self.browser = browser

    def delay(self): # random delay to help preventing detection
        time.sleep(random.uniform(0.0,5.5))
    
    def prepare_options(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("user-data-dir=argyleisawesome")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        return options

    def prepare_browser(self):
        options = self.prepare_options()
        cwd = os.getcwd()
        DRIVER_PATH = cwd + './chromedriver_win32_hacked/chromedriver.exe'
        browser = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
        browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
        return browser

    def wait_for_field_by_id(self, id):
        delay = self.DELAY # seconds
        try:
            print("Waiting "+id)    
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.ID, id)))
        except TimeoutException:
            print("Field loading took too much time!")  

    def wait_for_field_by_name(self, name):
        delay = self.DELAY # seconds
        try:
            print("Waiting "+name)    
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.NAME, name)))
        except TimeoutException:
            print("Field loading took too much time!")  

    def wait_for_field_by_xpath(self, xpath):
        delay = self.DELAY # seconds
        try:
            print("Waiting "+xpath)    
            myElem = WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print("Field loading took too much time!")  

    def wait_for_field_visibility_by_id(self, id):
        delay = self.DELAY # seconds
        try:
            print("Waiting visibility "+id)    
            myElem = WebDriverWait(self.browser, delay).until(EC.visibility_of_element_located((By.ID, id)))
        except TimeoutException:
            print("Field loading took too much time!")  

    def wait_for_field_visibility_by_name(self, name):
        delay = self.DELAY # seconds
        try:
            print("Waiting visibility "+name)    
            myElem = WebDriverWait(self.browser, delay).until(EC.visibility_of_element_located((By.NAME, name)))
        except TimeoutException:
            print("Field loading took too much time!")  

    def wait_for_field_visibility_xpath(self, xpath):
        delay = self.DELAY # seconds
        try:
            print("Waiting visibility "+xpath)    
            myElem = WebDriverWait(self.browser, delay).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print("Field loading took too much time!")  

    def prepare_input_by_id(self, id, newvalue):
        self.wait_for_field_by_id(id)
        element = self.browser.find_element_by_id(id)
        self.delay()
        element.send_keys(newvalue)

    def prepare_input_by_name(self, name, newvalue):
        self.wait_for_field_by_name(name)
        element = self.browser.find_element_by_name(name)
        self.delay()
        element.send_keys(newvalue)

    def prepare_input_by_xpath(self, xpath, newvalue):
        self.wait_for_field_by_xpath(xpath)
        element = self.browser.find_element_by_xpath(xpath)
        self.delay()
        element.send_keys(newvalue)

    def click_button_by_id(self, id):
        self.wait_for_field_by_id(id)
        button = self.browser.find_element_by_id(id)
        self.delay()
        button.click()

    def click_button_by_name(self, name):
        self.wait_for_field_by_name(name)
        button = self.browser.find_element_by_name(name)
        self.delay()
        button.click()

    def click_button_by_xpath(self, xpath):
        self.wait_for_field_by_xpath(xpath)
        button = self.browser.find_element_by_xpath(xpath)
        self.delay()
        button.click()

    def try_get_element_by_name(self, name):
        try:
            self.wait_for_field_by_name(name)
            element = self.browser.find_element_by_name(name)
            return element
        except NoSuchElementException:
            return None

    def try_get_element_by_id(self, id):
        try:
            self.wait_for_field_by_id(id)
            element = self.browser.find_element_by_id(id)
            return element
        except NoSuchElementException:
            return None

    def try_get_element_by_xpath(self, xpath):
        try:
            self.wait_for_field_by_xpath(xpath)
            element = self.browser.find_element_by_xpath(xpath)
            return element
        except NoSuchElementException:
            return None

    def get_input_value_by_xpath(self, id):
        input = self.try_get_element_by_id(id)
        value = input.get_attribute('value')
        return value

    def get_input_value_by_xpath(self, name):
        input = self.try_get_element_by_name(name)
        value = input.get_attribute('value')
        return value

    def get_input_value_by_xpath(self, xpath):
        input = self.try_get_element_by_xpath(xpath)
        value = input.get_attribute('value')
        return value

    def quit(self):
        self.browser.quit()