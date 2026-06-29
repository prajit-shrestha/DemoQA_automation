from config.config import BASE_URL
from pages.home_page import HomePage
import logging

def test_home_page(driver):
    logging.info("Starting homepage test case")
    home = HomePage(driver)

    home.open_home_page(BASE_URL)

    assert "demoqa" in driver.current_url