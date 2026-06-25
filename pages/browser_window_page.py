from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BrowserWindowsPage:

    NEW_TAB_BUTTON = (By.ID, "tabButton")
    NEW_WINDOW_BUTTON = (By.ID, "windowButton")
    RESULT_TEXT = (By.ID, "sampleHeading")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def click_new_tab(self):
        self.driver.find_element(*self.NEW_TAB_BUTTON).click()

    def click_new_window(self):
        wait = WebDriverWait(self.driver, 10)

        window_button = wait.until(
            EC.element_to_be_clickable((By.ID, "windowButton"))
        )

        window_button.click()

    def switch_to_new_tab(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    def switch_to_parent(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    def get_result_text(self):
        return self.driver.find_element(*self.RESULT_TEXT).text