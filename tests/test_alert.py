from pages.alert_page import AlertPage
from config.config import BASE_URL
from pages.home_page import HomePage
from pages.alert_frame_windows import AlertFrameWindows
from pages.alert_page import AlertPage

def test_alert(driver):
    driver.get(BASE_URL)

    home = HomePage(driver)
    home.open_home_page(BASE_URL)

    afw = AlertFrameWindows(driver)
    afw.click_alert_frame_window()

    #Alert page
    alert_page = AlertPage(driver)
    alert_page.click_alert_menu()
    alert_page.simple_alert()

    #Switch to alert
    alert_page.get_alert_text()
    assert_text = alert_page.get_alert_text().lower()
    assert assert_text == "you clicked a button"

    alert_page.accept_alert()

