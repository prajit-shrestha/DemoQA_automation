import pytest

from pages.Widgets.accordion_page import AccordionPage
from config.config import BASE_URL
from pages.home_page import HomePage
from pages.Widgets.widget_menu_page import Widget_Page


@pytest.mark.parametrize("section,expected_text", [
    (1, "Lorem Ipsum"),
    (2, "Contrary"),
    (3, "established")
])
def test_accordion_sections(driver, section, expected_text):

    driver.get(BASE_URL)

    home = HomePage(driver)
    home.open_home_page(BASE_URL)

    widget_menu_page = Widget_Page(driver)
    widget_menu_page.open_widgets()

    accordion = AccordionPage(driver)
    accordion.open_accordion_menu()
    accordion.remove_ads()

    accordion.click_section(section)
    accordion.remove_ads()

    text = accordion.get_section_text(section)

    assert expected_text in text