import logging
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

LOG = logging.getLogger(__name__)


class FindElement:
    def __init__(self, driver: Chrome):
        self.driver = driver

    def by_css_selector(self, locator: str):
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        LOG.info("element_by_css_celector %s", element)
        return element

    def list_by_tag_name(self, locator: str):
        elements = self.driver.find_elements(By.TAG_NAME, locator)
        LOG.info("elements_by_tag %s", elements)
        return elements

    def by_id(self, locator: str):
        element = self.driver.find_element(By.ID, locator)
        LOG.info("element_by_id %s", element)
        return element

    def by_xpath(self, locator: str):
        element = self.driver.find_element(By.XPATH, locator)
        LOG.info("element_by_xpath %s", element)
        return element

    def list_by_xpath(self, locator: str):
        elements = self.driver.find_elements(By.XPATH, locator)
        LOG.info("elements_by_xpath %s", elements)
        return elements

    def list_by_css_selector(self, locator: str):
        elements = self.driver.find_elements(By.CSS_SELECTOR, locator)
        LOG.info("elements_by_css_selector %s", elements)
        return elements

    def by_row_index_and_column_index(self, row_index: int, column_index: int):
        """
        Gets element by row and column indexes
        @param row_index: row index int
        @param column_index: column index int
        @return: element
        """
        element = self.by_css_selector(
            f"tr:nth-child({row_index}) > td:nth-child({column_index})"
        )
        LOG.info("element by css selector and tr,td indexes  %s", element)
        return element

    def th_column_index_by_text(self, text: str) -> int:
        """
        Gets table header column index when we know row number
        @param text: text of table field str
        @return: column index int
        """
        elements = self.list_by_xpath("//table/thead/tr/th")
        LOG.info("elements by xpath  %s", elements)
        elements_text = [el.text for el in elements]
        LOG.info("elements texts %s", elements_text)
        index = elements_text.index(text)
        LOG.info("element %s column index is: %s", text, index)
        column_index = index + 1
        LOG.info("table header column index: %s", column_index)
        return column_index

    def tbody_row_index_by_text(self, text: str) -> list:
        """
        Gets table body row index by text of table field
        @param text: text of table field str
        @return: column index int
        """
        elements = self.list_by_xpath("//table/tbody/tr")
        LOG.info("elements by xpath %s", elements)
        row_elements_text = [el.text for el in elements]
        LOG.info("elements text %s", row_elements_text)
        row_index = [i for i, e in enumerate(row_elements_text) if text in e][0]
        LOG.info("element %s row index is: %s", text, row_index)
        row_index = row_index + 1
        LOG.info("table body row index: %s", row_index)
        return [row_index, row_elements_text]

    def by_tbody_field_text(self, text: str):
        """
        Finds element table body row and column index by text of table field
        @param text: text of table field str
        @return: column index int
        """
        row_index = self.tbody_row_index_by_text(text)[0]
        row_elements_text = self.tbody_row_index_by_text(text)[1]
        row_el_list = row_elements_text[row_index - 1].split()
        LOG.info("row elemenent list: %s", row_el_list)
        column_index = [i for i, e in enumerate(row_el_list) if text in e][0]
        LOG.info("column index: %s", column_index)
        column_location = column_index + 1
        LOG.info("table body column location: %s", column_location)
        element = self.by_row_index_and_column_index(row_index, column_location)
        return element

    def by_text_in_tbody_row_and_xpath(self, text: str, xpath: str):
        """
        Finds element by text in table body row and xpath
        @param text: text of table field in raw str
        @param xpath: xpath str
        @return: element
        """
        row_index = self.tbody_row_index_by_text(text)[0]
        element = self.by_xpath(f"//table/tbody/tr[{row_index}]/td{xpath}")
        LOG.info("element text %s", element.text)
        return element

    def green_button(self):
        """
        Finds green button element by css selector - ".button.success"
        @return: element
        """
        element = self.by_css_selector(".button.success")
        LOG.info("green button element text %s", element.text)
        return element

    def finding_iframe(self):
        """
        Finds iframe which we need to use. It is third iframe element
        @return: element
        """
        return self.list_by_xpath("//iframe")[3]
