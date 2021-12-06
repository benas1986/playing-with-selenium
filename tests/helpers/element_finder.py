import logging

from selenium import webdriver
from selenium.webdriver.common.by import By

LOG = logging.getLogger(__name__)


class FindElement:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.row_location = None
        self.row_elements_text = None
        self.row_location_index = None

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

    def by_css_selector_and_tr_and_td(self, row_location: int, column_location: int):
        """
        Gets element by row and column locations
        @param row_location: row location number int
        @param column_location: column location number int
        @return: element
        """
        element = self.by_css_selector(
            f"tr:nth-child({row_location}) > td:nth-child({column_location})"
        )
        LOG.info("element by css selector and tr,td locations  %s", element)
        return element

    def table_header_column_location_by_text(self, text: str) -> int:
        """
        Gets table header column location number when we know row number
        @param text: text of table field str
        @return: column location number int
        """
        elements = self.list_by_xpath("//table/thead/tr/th")
        LOG.info("elements by xpath  %s", elements)
        elements_text = [el.text for el in elements]
        LOG.info("elements texts %s", elements_text)
        index = elements_text.index(text)
        LOG.info("element %s column index is: %s", text, index)
        column_location = index + 1
        LOG.info("table header column location: %s", column_location)
        return column_location

    def table_body_row_location_by_text(self, text: str) -> int:
        """
        Gets table body row location number by text of table field
        @param text: text of table field str
        @return: column location number int
        """
        elements = self.list_by_xpath("//table/tbody/tr")
        LOG.info("elements by xpath %s", elements)
        self.row_elements_text = [el.text for el in elements]
        LOG.info("elements text %s", self.row_elements_text)
        self.row_location_index = [
            i for i, e in enumerate(self.row_elements_text) if text in e
        ][0]
        LOG.info("element %s row index is: %s", text, self.row_location_index)
        self.row_location = self.row_location_index + 1
        LOG.info("table body row location: %s", self.row_location)
        return self.row_location

    def by_table_body_field_text(self, text: str):
        """
        Finds element table body row and column location number by text of table field
        @param text: text of table field str
        @return: column location number int
        """
        self.table_body_row_location_by_text(text)
        row_el_list = self.row_elements_text[self.row_location_index].split()
        LOG.info("row elemenent list: %s", row_el_list)
        column_index = [i for i, e in enumerate(row_el_list) if text in e][0]
        LOG.info("column index: %s", column_index)
        column_location = column_index + 1
        LOG.info("table body column location: %s", column_location)
        element = self.by_css_selector_and_tr_and_td(self.row_location, column_location)
        return element

    def by_text_in_table_body_row_and_xpath(self, text: str, el_xpath: str):
        """
        Finds element by text in table body row and xpath
        @param text: text of table field in raw str
        @param el_xpath: xpath str
        @return: element
        """
        self.row_location = self.table_body_row_location_by_text(text)
        element = self.by_xpath(f"//table/tbody/tr[{self.row_location}]/td{el_xpath}")
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
        return self.driver.find_elements(By.XPATH, "//iframe")[3]
