from pages.Base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AutoCompletePage(BasePage):
    #locator
    AUTO_MENU = (By.XPATH, "//span[normalize-space()='Auto Complete']")
    MULTI_INPUT = (By.ID,"autoCompleteMultipleInput")
    SINGLE_INPUT = (By.ID,"autoCompleteSingleInput")

    SELECTED_COLORS = (By.CSS_SELECTOR,".auto-complete__multi-value__label")
    SINGLE_SELECTED_COLOR = (By.CSS_SELECTOR,".auto-complete__single-value")
    #Click menu Method
    def click_auto_menu(self):
        self.wait_for_clickable(self.AUTO_MENU).click()

    #Multi input
    def enter_multiple_colors(self,colors):
        input_box = self.wait_for_element(self.MULTI_INPUT)
        for color in colors:
            input_box.send_keys(color)
            input_box.send_keys(Keys.ENTER)

    def get_selected_colors(self):
        elements = self.driver.find_elements(*self.SELECTED_COLORS)
        return [element.text for element in elements]

    #SINGLE INPUT
    def enter_single_color(self,color):
        input_box = self.wait_for_element(self.SINGLE_INPUT)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            input_box
        )
        input_box.send_keys(color)
        input_box.send_keys(Keys.ENTER)

    def get_single_color(self):
        return self.wait_for_element(
            self.SINGLE_SELECTED_COLOR
        ).text