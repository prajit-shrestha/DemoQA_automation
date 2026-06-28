from pages.Base_page import BasePage
from selenium.webdriver.common.by import By

class ModalDialogsPage(BasePage):

    # locator
    MODAL_DIALOGS_MENU = (By.XPATH, "//span[text()='Modal Dialogs']")
    SMALL_MODAL_BUTTON = (By.ID, "showSmallModal")
    LARGE_BUTTON = (By.ID, "showLargeModal")

    SMALL_TEXT = (By.CLASS_NAME, "modal-body")
    LARGE_TEXT = (By.CLASS_NAME, "modal-body")

    CLOSE_BUTTON = (By.ID, "closeSmallModal")
    LARGE_CLOSE_BUTTON = (By.ID, "closeLargeModal")


    # navigation
    def click_modal_dialog_menu(self):
        element = self.wait_for_element(self.MODAL_DIALOGS_MENU)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

        # FORCE click via JS to bypass footer overlay
        self.driver.execute_script("arguments[0].click();", element)

    # actions
    def click_small_modal_button(self):
        self.wait_for_clickable(self.SMALL_MODAL_BUTTON).click()

    def click_large_modal_button(self):
        self.wait_for_clickable(self.LARGE_BUTTON).click()

    # texts
    def get_small_modal_text(self):
        return self.wait_for_element(self.SMALL_TEXT).text

    def get_large_modal_text(self):
        return self.wait_for_element(self.LARGE_TEXT).text

    # close actions
    def click_close_button(self):
        self.wait_for_element(self.CLOSE_BUTTON).click()

    def click_large_close_button(self):
        self.wait_for_element(self.LARGE_CLOSE_BUTTON).click()