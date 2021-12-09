import logging

from pytest import fixture
from selenium.webdriver import Chrome

from tests.helpers.chrome_browser import ChromeDriver
from tests.helpers.element_actions import ElementActions
from tests.helpers.element_finder import FindElement

LOG = logging.getLogger(__name__)


@fixture(scope="session")
def chrome_driver():
    driver = ChromeDriver()
    yield driver.start()
    driver.stop()


@fixture(scope="session")
def element_finder(chrome_driver: Chrome):
    return FindElement(chrome_driver)


@fixture(scope="session")
def element_actions(chrome_driver: Chrome):
    return ElementActions(chrome_driver)
