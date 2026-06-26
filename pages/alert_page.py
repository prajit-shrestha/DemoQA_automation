
from selenium.webdriver.common.by import By
from pages.Base_page import BasePage

class AlertPage(BasePage):

    #LOACTOR
    ALERT_MENU = (By.XPATH, "//span[normalize-space()='Alerts']")
    ALERT_BUTTON = (By.ID, "alertButton")
    TIMER_ALERT_BUTTON = (By.ID,"timerAlertButton")
    CONFIRM_BUTTON = (By.ID,"confirmButton")
    PROMPT_BUTTON = (By.ID,"promptButton")

    #NAVIGATION
    def click_alert_menu(self):
        self.wait_for_clickable(self.ALERT_MENU).click()

    #ACTION
    def simple_alert(self):
        self.wait_for_clickable(self.ALERT_BUTTON).click()

    def click_timer_btn(self):
        self.wait_for_clickable(self.TIMER_ALERT_BUTTON).click()

    def confirm_alert_btn(self):
        self.wait_for_clickable(self.CONFIRM_BUTTON).click()

    def prompt_alert_btn(self):
        self.wait_for_clickable(self.PROMPT_BUTTON).click()

    #Alert handling
    def get_alert_text(self):
        return self.driver.switch_to.alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def wait_for_timer_alert(self):
        self.wait_for_alert()
