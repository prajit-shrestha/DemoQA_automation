from selenium.webdriver.common.by import By
from pages.Base_page import BasePage

class Widget_Page(BasePage):

    # Locators
    HOME_WIDGET = (By.XPATH, "//a[@href='/widgets']//div[@class='card mt-4 top-card']//div//div[@class='card-body']")
    WIDGET_MENU = (By.XPATH, "//div[text()='Widgets']")

    ACCORDIAN = (By.XPATH, "//span[text()='Accordian']")
    AUTO_COMPLETE = (By.XPATH, "//span[text()='Auto Complete']")
    DATE_PICKER = (By.XPATH, "//span[text()='Date Picker']")
    SLIDER = (By.XPATH, "//span[text()='Slider']")
    PROGRESS_BAR = (By.XPATH, "//span[text()='Progress Bar']")
    TAB = (By.XPATH, "//span[text()='Tabs']")
    TOOL_TIPS = (By.XPATH, "//span[normalize-space()='Tool Tips']")
    MENU = (By.XPATH, "//span[normalize-space()='Menu']")
    SELECT_MENU = (By.XPATH, "//span[text()='Select Menu']")

    # Click methods
    def open_widgets(self):
        self.scroll_to_element(self.HOME_WIDGET).click()


    def open_widget_menu(self):
        self.wait_for_clickable(self.WIDGET_MENU).click()

    # Visibility checks
    def is_visible(self, locator):
        element = self.scroll_to_element(locator)
        return element.is_displayed()

    def is_display_accordian(self):
        return self.is_visible(self.ACCORDIAN)

    def is_display_auto_complete(self):
        return self.is_visible(self.AUTO_COMPLETE)

    def is_display_date_picker(self):
        return self.is_visible(self.DATE_PICKER)

    def is_display_slider(self):
        return self.is_visible(self.SLIDER)

    def is_display_progress_bar(self):
        return self.is_visible(self.PROGRESS_BAR)

    def is_display_tab(self):
        return self.is_visible(self.TAB)

    def is_display_tool_tips(self):
        return self.is_visible(self.TOOL_TIPS)

    def is_display_menu(self):
        return self.is_visible(self.MENU)

    def is_display_select_menu(self):
        return self.is_visible(self.SELECT_MENU)