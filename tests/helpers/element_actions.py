import logging
import time

from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains

LOG = logging.getLogger(__name__)


class ElementActions:
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.width = None
        self.height = None

    def width_and_height(self, element) -> [int, int]:
        """
        Gets element weight and height
        @param element: text of table field object
        @return: width int and height
        """
        size = element.size
        LOG.info("element size %s", size)
        self.width, self.height = size["width"] + 4, size["height"]
        LOG.info("element width %s and height %s", self.width, self.width)
        return self.width, self.height

    def highlight_text(self, element, duration):
        """
        Highlights text element
        @param element: element object
        @param duration: duration int
        """
        self.actions.double_click(element)
        self.actions.perform()
        time.sleep(duration)
        self.actions.click()
        self.actions.perform()

    def highlight_link(self, element, duration):
        """
        Highlights link element
        @param element: element object
        @param duration: duration int
        """
        self.width, self.height = self.width_and_height(element)
        self.actions.move_to_element(element)
        self.actions.move_by_offset(-self.height, -10)
        self.actions.click_and_hold()
        self.actions.move_by_offset(self.width, 10)
        self.actions.perform()
        time.sleep(duration)
        self.actions.click()
        self.actions.perform()

    def click(self, element):
        """
        Clicks element
        @param element: element object
        """
        self.actions.click(element)
        self.actions.perform()

    @staticmethod
    def input_text(element, text):
        """
        Inserts text into element
        @param element: element object
        @param text: text any
        """
        element.send_keys(text)
