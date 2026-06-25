from pages.home_page import HomePage
from pages.alert_frame_windows import AlertFrameWindows
from config.config import BASE_URL

def test_alert_frame_window(driver):
    driver.get(BASE_URL)

    #home
    home = HomePage(driver)
    home.open_home_page(BASE_URL)

    #Click alert frame window
    afw = AlertFrameWindows(driver)
    afw.click_alert_frame_window()

    assert "alertsWindows" in driver.current_url, "Navigation failed"
    assert afw.is_browser_visible()
    assert afw.is_alerts_visible()
    assert afw.is_frames_visible()
    assert afw.is_nested_frames_visible()
    assert afw.is_modal_dialogs_visible()