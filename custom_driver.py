import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from devices import Devices

class CustomDriver:
    def __init__(self, instruction, fullscreen = False):
        chromedriver = os.path.dirname(os.path.realpath(__file__)) + '/chromedriver'
        sc_width, sc_height = Devices().get(instruction.device)
        options = Options()
        options.add_argument(f'window-size={sc_width}x{sc_height}')
        options.headless = instruction.headless
        options.add_argument('disable_infobars')

        self.sc_width = sc_width
        self.sc_height = sc_height
        self.driver = webdriver.Chrome(chromedriver, options=options)

    def get(self, url):
        return self.driver.get(url)

    def save_screenshot(self, path):
        return self.driver.save_screenshot(path)

    def save_full_page_screenshot(self, path):
        time.sleep(0.3)
        # S = lambda X: self.driver.execute_script('return document.querySelector("body").scroll'+X)
        S = lambda X: self.driver.execute_script('return document.documentElement.scroll'+X)

        self.driver.set_window_size(S('Width'), S('Height'))
        time.sleep(0.2)
        self.driver.find_element_by_tag_name('body').screenshot(path)
        time.sleep(0.2)
        self.driver.set_window_size(self.sc_width, self.sc_height)
        time.sleep(0.2)

    def quit(self):
        return self.driver.quit()

    def find_element(self, selector):
        return self.driver.find_element(by='css selector', value=selector)

    def find_elements(self, selector):
        return self.driver.find_elements(by='css selector', value=selector)

    def wait_and_see(self, selector, timeout = 3):
        element_present = EC.presence_of_element_located(('css selector', selector))
        WebDriverWait(self.driver, timeout).until(element_present)
        time.sleep(0.2)

    def wait_and_dont_see(self, selector, timeout = 3):
        element_invisible = EC.invisibility_of_element_located(('css selector', selector))
        WebDriverWait(self.driver, timeout).until(element_invisible)
        time.sleep(0.2)
