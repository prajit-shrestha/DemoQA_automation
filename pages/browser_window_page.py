from selenium.webdriver.common.by import By
from pages.Base_page import BasePage

class BrowserWindowsPage(BasePage):

    BROWSER_WINDOWS = (By.XPATH, "//span[normalize-space()='Browser Windows']")
    NEW_TAB_BUTTON = (By.ID, "tabButton")
    NEW_WINDOW_BUTTON = (By.ID, "windowButton")
    NEW_WINDOW_MESSAGE_BUTTON = (By.ID, "messageWindowButton")
    RESULT_TEXT = (By.ID, "sampleHeading")

    def click_browser_windows(self):
        self.wait_for_clickable(self.BROWSER_WINDOWS).click()

    def click_new_tab(self):
        self.wait_for_clickable(self.NEW_TAB_BUTTON).click()

    def click_new_window(self):
        self.wait_for_clickable(self.NEW_WINDOW_BUTTON).click()

    def click_new_window_message(self):
        self.wait_for_clickable(self.NEW_WINDOW_MESSAGE_BUTTON).click()

#Switching
    def switch_to_new_window(self):
        parent = self.driver.current_window_handle  # save current window

        for handle in self.driver.window_handles:
            if handle != parent:
                self.driver.switch_to.window(handle)
                break

    def switch_to_parent(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_text(self):
        return self.driver.find_element(*self.RESULT_TEXT).text