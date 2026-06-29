from selenium.webdriver.common.by import By
from pages.Base_page import BasePage


class FramePage(BasePage):

    # Locators
    FRAME_MENU_BUTTON = (By.XPATH, "//span[text()='Frames']")
    FRAME_1 = (By.ID, "frame1")
    FRAME_2 = (By.ID, "frame2")
    RESULT_TEXT = (By.ID,"sampleHeading")

    # Navigation
    def click_menu_frame(self):
        self.wait_for_clickable(self.FRAME_MENU_BUTTON).click()

    # Switch Frame 1
    def switch_to_frame1(self):
        frame = self.wait_for_element(self.FRAME_1)
        self.driver.switch_to.frame(frame)

    # Switch Frame 2
    def switch_to_frame2(self):
        frame = self.wait_for_element(self.FRAME_2)
        self.driver.switch_to.frame(frame)

    # Back to main page
    def switch_to_default(self):
        self.driver.switch_to.default_content()

    # Get text inside frame
    def get_result_text(self):
        return self.wait_for_element(self.RESULT_TEXT).text