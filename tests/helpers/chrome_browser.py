import logging

import chromedriver_autoinstaller
from selenium import webdriver

LOG = logging.getLogger(__name__)

chromedriver_autoinstaller.install("playing_with_selenium/tests/helpers")


class ChromeDriver:
    def __init__(self):
        self.driver = None

    def start(self):
        LOG.debug("CONNECTING TO CHROME DRIVER")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        return self.driver

    def stop(self):
        LOG.debug("CLOSING CHROME DRIVER")
        return self.driver.quit()
