from selenium.webdriver.common.by import By
from pages.Base_page import BasePage


class AccordionPage(BasePage):

    ACCORDION_MENU = (By.XPATH, "//span[normalize-space()='Accordian']")

    SECTION_1_HEADER = (By.XPATH, "//button[contains(text(),'What is Lorem')]")
    SECTION_2_HEADER = (By.XPATH, "//button[contains(text(),'Where does it come from')]")  # XPath by text - most reliable
    SECTION_3_HEADER = (By.XPATH, "//button[contains(text(),'Why do we use it')]")

    SECTION_1_CONTENT = (By.XPATH, "//p[contains(text(),'Lorem Ipsum')]")
    SECTION_2_CONTENT = (By.XPATH, "//p[contains(text(),'Contrary')]")
    SECTION_3_CONTENT = (By.XPATH, "//p[contains(text(),'established')]")

    def open_accordion_menu(self):
        self.wait_for_clickable(self.ACCORDION_MENU).click()

    def click_section(self, section_number):
        headers = {
            1: self.SECTION_1_HEADER,
            2: self.SECTION_2_HEADER,
            3: self.SECTION_3_HEADER,
        }
        if section_number not in headers:
            raise Exception(f"Invalid section number: {section_number}")

        element = self.wait_for_clickable(headers[section_number])

        element.click()

    def get_section_text(self, section_number):
        locators = {
            1: self.SECTION_1_CONTENT,
            2: self.SECTION_2_CONTENT,
            3: self.SECTION_3_CONTENT,
        }
        if section_number not in locators:
            raise Exception("Invalid section")

        return self.wait_for_element(locators[section_number]).text