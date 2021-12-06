import logging

from tests.helpers.element_actions import ElementActions
from tests.helpers.element_finder import FindElement

LOG = logging.getLogger(__name__)

# traversing table elements firstly by rows and then by columns


def test_web_table(
    chrome_driver, element_finder: FindElement, element_actions: ElementActions
):
    LOG.info("STEP 1")
    LOG.info("OPENING WEB PAGE")
    chrome_driver.get("http://the-internet.herokuapp.com/challenging_dom")

    LOG.info("STEP 2")
    LOG.info("HIGHLIGHTING THE TEXT IN THE THIRD ROW AND Diceret COLUMN")
    text = "Diceret"
    row_location = 3
    column_location = element_finder.table_header_column_location_by_text(text)
    phaedrum2_element = element_finder.by_css_selector_and_tr_and_td(
        row_location, column_location
    )
    element_actions.highlight_text(phaedrum2_element)
    assert phaedrum2_element.text == "Phaedrum2"

    LOG.info("STEP 3")
    LOG.info("HIGHLIGHTING THE DELETE LINK IN THE ROW CONTAINING Apeirian7")
    text = "Apeirian7"
    delete_element_xpath = "//a[@href='#delete']"
    apeirian7_element = element_finder.by_text_in_table_body_row_and_xpath(
        text, delete_element_xpath
    )
    element_actions.highlight_link(apeirian7_element)
    assert apeirian7_element.text == "delete"

    LOG.info("STEP 4")
    LOG.info("HIGHLIGHTING THE EDIT LINK IN THE ROW CONTAINING Apeirian2")
    text = "Apeirian2"
    edit_element_xpath = "//a[@href='#edit']"
    apeirian2_element = element_finder.by_text_in_table_body_row_and_xpath(
        text, edit_element_xpath
    )
    element_actions.highlight_link(apeirian2_element)
    assert apeirian2_element.text == "edit"

    LOG.info("STEP 5")
    LOG.info("HIGHLIGHTING Definiebas7")
    text = "Definiebas7"
    definiebas7_element = element_finder.by_table_body_field_text(text)
    element_actions.highlight_text(definiebas7_element)
    assert definiebas7_element.text == text

    LOG.info("HIGHLIGHTING Iuvaret7")
    text = "Iuvaret7"
    iuvaret7_element = element_finder.by_table_body_field_text(text)
    element_actions.highlight_text(iuvaret7_element)
    assert iuvaret7_element.text == text

    LOG.info("STEP 6")
    LOG.info("CLICKING THE GREEN BUTTON")
    button_element = element_finder.green_button()
    element_actions.click(button_element)
