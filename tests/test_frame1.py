from pages.frame.framepage import FramePage
from config.config import BASE_URL
from pages.home_page import HomePage
from pages.alert_frame_windows import AlertFrameWindows


def test_alert_cancel(driver):
    driver.get(BASE_URL)
    #home
    home = HomePage(driver)
    home.open_home_page(BASE_URL)
    #menus
    afw = AlertFrameWindows(driver)
    afw.click_alert_frame_window()


    frame = FramePage(driver)
    frame.click_menu_frame()
    frame.switch_to_frame1()
    #getting the test
    text = frame.get_result_text()

    #assert
    assert "this is a sample page" in text.lower(),f"Expected sample page text, but got:{text}"

    #back to main page
    frame.switch_to_default()



