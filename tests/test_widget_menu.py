from pages.home_page import HomePage
from pages.Widgets.widget_menu_page import Widget_Page
from config.config import BASE_URL
import logging


def test_widget_page(driver):

    driver.get(BASE_URL)

    home = HomePage(driver)

    logging.info("Clicking widgets")
    widget = Widget_Page(driver)

    widget.open_widgets()
    widget.remove_ads()
    widget.open_widget_menu()
    widget.remove_ads()

    logging.info("Checking widget visibility")

    assert widget.is_display_accordian(), "Accordion not visible"
    assert widget.is_display_auto_complete(), "Auto complete not visible"
    assert widget.is_display_date_picker(), "Date picker not visible"
    assert widget.is_display_slider(), "Slider not visible"
    assert widget.is_display_progress_bar(), "Progress bar not visible"
    assert widget.is_display_tab(), "Tab not visible"
    assert widget.is_display_tool_tips(), "Tool tips not visible"
    assert widget.is_display_menu(), "Menu not visible"
    assert widget.is_display_select_menu()





