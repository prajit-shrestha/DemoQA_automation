from config.config import BASE_URL
from pages.home_page import HomePage

def test_home_page(driver):

    home = HomePage(driver)

    home.open_home_page(BASE_URL)

    assert "demoqa" in driver.current_url