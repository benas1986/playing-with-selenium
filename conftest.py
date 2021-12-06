import logging

from pytest import fixture

from tests.helpers.chrome_browser import ChromeDriver
from tests.helpers.element_actions import ElementActions
from tests.helpers.element_finder import FindElement
from selenium.webdriver.chrome import webdriver

LOG = logging.getLogger(__name__)


@fixture(scope="session")
def chrome_driver():
    driver = ChromeDriver().chrome_driver_start()
    yield driver
    LOG.debug("CLOSING CHROME DRIVER")
    driver.quit()


@fixture(scope="session")
def element_finder(chrome_driver: webdriver):
    return FindElement(chrome_driver)


@fixture(scope="session")
def element_actions(chrome_driver: webdriver):
    return ElementActions(chrome_driver)
