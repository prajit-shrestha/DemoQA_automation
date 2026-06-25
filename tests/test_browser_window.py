import time

from pages.browser_window_page import BrowserWindowsPage
from config.config import BASE_URL
from pages.alert_frame_windows import AlertFrameWindows
from pages.home_page import HomePage
from pages.browser_window_page import BrowserWindowsPage


def test_new_tab(driver):
    driver.get(BASE_URL)

    home = HomePage(driver)
    home.open_home_page(BASE_URL)

    afw = AlertFrameWindows(driver)
    afw.click_alert_frame_window()

    browser = BrowserWindowsPage(driver)
    browser.click_browser_windows()

    # NEW TAB
    browser.click_new_tab()
    time.sleep(2)
    browser.switch_to_new_window()
    time.sleep(2)
    assert "sample page" in browser.get_text().lower()
    # back to parent
    browser.switch_to_parent()

    # NEW WINDOW
    browser.click_new_window()
    time.sleep(2)
    browser.switch_to_new_window()
    time.sleep(2)
    assert "sample page" in browser.get_text().lower()
    browser.switch_to_parent()

    #Window Message
    browser.click_new_window_message()
    time.sleep(2)
    browser.switch_to_new_window()
    text = browser.get_text()
    assert text is not None
    assert len(text) > 0

    browser.switch_to_parent()