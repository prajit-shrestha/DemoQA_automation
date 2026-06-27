
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.Base_page import BasePage


class AlertFrameWindows(BasePage):

    alert_frame_windows = (By.XPATH,"//h5[normalize-space()='Alerts, Frame & Windows']")

    BROWSER_WINDOWS = (By.XPATH, "//span[text() = 'Browser Windows']")
    ALERTS = (By.XPATH, "//span[text()='Alerts']")
    FRAMES = (By.XPATH, "//span[text()='Frames']")
    NESTED_FRAMES = (By.XPATH, "//span[text()='Nested Frames']")
    MODAL_DIALOGS = (By.XPATH, "//span[text()='Modal Dialogs']")


    def click_alert_frame_window(self):
        element = self.scroll_to_element(self.alert_frame_windows)
        element.click()

    def is_browser_visible(self):
        return self.wait_for_element(
            self.BROWSER_WINDOWS
        ).is_displayed()
    def is_frames_visible(self):
        return self.wait_for_element(
            self.FRAMES
        ).is_displayed()

    def is_alerts_visible(self):
        return self.wait_for_clickable(self.ALERTS).is_displayed()

    def is_nested_frames_visible(self):
        return self.wait_for_clickable(self.NESTED_FRAMES).is_displayed()

    def is_modal_dialogs_visible(self):
        return self.wait_for_clickable(self.MODAL_DIALOGS).is_displayed()