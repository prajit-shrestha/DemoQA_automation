from pages.browser_window_page import BrowserWindowsPage
from config.config import Base_URL


def test_new_tab(driver):

    page = BrowserWindowsPage(driver)

    # Open page
    page.open_page(Base_URL)

    # Click new tab
    page.click_new_tab()

    # Switch tab
    page.switch_to_new_tab()

    # Get text
    text = page.get_result_text()

    # Assertion
    assert "This is a sample page" in text