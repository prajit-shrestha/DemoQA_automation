from pages.Base_page import BasePage
from selenium.webdriver.common.by import By


class NestedFramePage(BasePage):
    #locator
    NESTED_FRAME_MENU = (By.XPATH,"//span[text()='Nested Frames']")
    PARENT_FRAME = (By.ID,"frame1")
    CHILD_Frame = (By.TAG_NAME,"iframe")
    RESULT_TEXT = (By.TAG_NAME,"p")

    #NAVIGATION
    def click_nested_frame(self):
        self.wait_for_clickable(self.NESTED_FRAME_MENU).click()

    #switching
    def switch_parent_frame(self):
        frame = self.wait_for_element(self.PARENT_FRAME)
        self.driver.switch_to.frame(frame)

    def switch_child_frame(self):
        frame = self.wait_for_element(self.CHILD_Frame)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def get_result_text(self):
        return self.wait_for_element(self.RESULT_TEXT).text
