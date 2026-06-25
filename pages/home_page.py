from selenium import webdriver
from config.config import BASE_URL

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self,url):
        self.driver.get(url)