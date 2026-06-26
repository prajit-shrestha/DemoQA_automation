from pages.alert_page import AlertPage
from config.config import BASE_URL
from pages.home_page import HomePage
from pages.alert_frame_windows import AlertFrameWindows
from pages.alert_page import AlertPage

def test_timer_alert(driver):
    driver.get(BASE_URL)
    #home
    home = HomePage(driver)
    home.open_home_page(BASE_URL)
    #menus
    afw = AlertFrameWindows(driver)
    afw.click_alert_frame_window()

    #Alert page
    alert_page = AlertPage(driver)
    alert_page.click_alert_menu()
    alert_page.click_timer_btn()
    alert_page.wait_for_timer_alert()

    #Switch to alert
    alert_page.get_alert_text()
    assert_text = alert_page.get_alert_text()
    assert assert_text == "This alert appeared after 5 seconds"

    alert_page.accept_alert()

