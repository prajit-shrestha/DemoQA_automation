import pytest
import logging
from selenium import webdriver

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

@pytest.fixture
def driver():
    logging.info("Launching Chrome browser")
    driver = webdriver.Chrome()

    logging.info("Browser launched and maximization")
    driver.maximize_window()
    yield driver

    logging.info("Browser closing ")
    driver.quit()