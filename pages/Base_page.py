from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_clickable(self,locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
    def wait_for_element(self,locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    def wait_for_alert(self):
        WebDriverWait(self.driver, 10).until(
            EC.alert_is_present()
        )

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        return element

    def remove_ads(self):
        """Remove DemoQA advertisements."""
        self.driver.execute_script("""
               let fixedBan = document.getElementById('fixedban');
               if (fixedBan) {
                   fixedBan.remove();
               }

               document.querySelectorAll('iframe').forEach(frame => {
                   try {
                       frame.remove();
                   } catch(e) {}
               });
           """)
