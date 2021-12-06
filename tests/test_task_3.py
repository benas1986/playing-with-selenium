import logging
import time

from selenium.webdriver.common.by import By

from tests.helpers.element_actions import ElementActions
from tests.helpers.element_finder import FindElement
from selenium.webdriver import Chrome

LOG = logging.getLogger(__name__)


def test_web_iframe(
    chrome_driver: Chrome, element_finder: FindElement, element_actions: ElementActions
):
    LOG.info("STEP 1")
    LOG.info("OPENING WEB PAGE")
    chrome_driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

    LOG.info("STEP 2")
    LOG.info("CLOSING THE BLUE DIALOG BOX")
    element = element_finder.by_css_selector(
        "div.single_tab_div.resp-tab-content.resp-tab-content-active > div > a"
    )
    element_actions.click(element)
    time.sleep(2)

    LOG.info("STEP 3")
    LOG.info("SWITCHING TO IFRAME")
    iframe = element_finder.finding_iframe()
    chrome_driver.switch_to.frame(iframe)
    LOG.info("COUNTING IMAGES")
    images = element_finder.list_by_tag_name("img")
    total_images = len(images)
    LOG.info("Count images %s", total_images)

    LOG.info("STEP 4")
    LOG.info("INSERTING TOTAL IMAGES COUNT INTO SEARCH")
    search_element = element_finder.by_id("s")
    LOG.info("Search element %s", search_element)
    element_actions.input_text(search_element, total_images)
    time.sleep(2)
