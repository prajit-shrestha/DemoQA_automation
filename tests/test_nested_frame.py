from pages.frame.framepage import FramePage
from config.config import BASE_URL
from pages.home_page import HomePage
from pages.alert_frame_windows import AlertFrameWindows
from pages.frame.nested_frame_page import NestedFramePage


def test_alert_cancel(driver):
    driver.get(BASE_URL)
    #home
    home = HomePage(driver)
    home.open_home_page(BASE_URL)
    #menus
    afw = AlertFrameWindows(driver)
    afw.click_alert_frame_window()


    #Nested frame
    NFP = NestedFramePage(driver)

    NFP.click_nested_frame()
    #parent
    NFP.switch_parent_frame()
    #child
    NFP.switch_child_frame()

    #getting result text
    text = NFP.get_result_text()

    #assertion
    assert "child iframe" in text.lower()

    NFP.switch_to_default_content()


