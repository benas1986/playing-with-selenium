import logging
import time

from selenium.webdriver import Chrome

from tests.helpers.element_actions import ElementActions
from tests.helpers.element_finder import FindElement

LOG = logging.getLogger(__name__)


def test_web_iframe(
    chrome_driver: Chrome, element_finder: FindElement, element_actions: ElementActions
):
    chrome_driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
    LOG.info("CLOSING THE BLUE DIALOG BOX")
    element = element_finder.by_css_selector(
        "div.single_tab_div.resp-tab-content.resp-tab-content-active > div > a"
    )
    element_actions.click(element)

    LOG.info("SWITCHING TO IFRAME")
    iframe = element_finder.finding_iframe()
    chrome_driver.switch_to.frame(iframe)
    LOG.info("COUNTING IMAGES")
    images = element_finder.list_by_tag_name("img")
    total_images = len(images)
    LOG.info("Total images %s", total_images)

    LOG.info("INSERTING TOTAL IMAGES COUNT INTO SEARCH")
    search_element = element_finder.by_id("s")
    LOG.info("Search element %s", search_element)
    element_actions.input_text(search_element, total_images)
    # added sleep to see the final result
    time.sleep(2)
