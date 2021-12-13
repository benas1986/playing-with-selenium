import logging
from selenium.webdriver import Chrome
from tests.helpers.element_actions import ElementActions
from tests.helpers.element_finder import FindElement

LOG = logging.getLogger(__name__)


def highlight_text_by_row_index_and_text(
    element_finder: FindElement,
    element_actions: ElementActions,
    text,
    row_index,
    duration,
):
    column_index = element_finder.th_column_index_by_text(text)
    element = element_finder.by_row_index_and_column_index(row_index, column_index)
    element_actions.highlight_text(element, duration)


def highlight_link_by_row_text_and_element_xpath(
    element_finder: FindElement, element_actions: ElementActions, text, xpath, duration
):
    element = element_finder.by_text_in_tbody_row_and_xpath(text, xpath)
    element_actions.highlight_link(element, duration)


def highlight_element_by_text(
    element_finder: FindElement, element_actions: ElementActions, text, duration
):
    element = element_finder.by_tbody_field_text(text)
    element_actions.highlight_text(element, duration)


def test_web_table(
    chrome_driver: Chrome, element_finder: FindElement, element_actions: ElementActions
):
    chrome_driver.get("http://the-internet.herokuapp.com/challenging_dom")
    highlight_text_by_row_index_and_text(
        element_finder, element_actions, "Diceret", row_index=3, duration=2
    )
    highlight_link_by_row_text_and_element_xpath(
        element_finder, element_actions, "Apeirian7", "//a[@href='#delete']", duration=2
    )
    highlight_link_by_row_text_and_element_xpath(
        element_finder, element_actions, "Apeirian2", "//a[@href='#edit']", duration=2
    )
    highlight_element_by_text(
        element_finder, element_actions, "Definiebas7", duration=2
    )
    highlight_element_by_text(element_finder, element_actions, "Iuvaret7", duration=2)

    green_button = element_finder.green_button()
    if green_button:
        element_actions.click(green_button)
