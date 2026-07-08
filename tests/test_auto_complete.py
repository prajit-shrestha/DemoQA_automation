import pytest
from pages.Widgets.auto_complete_page import AutoCompletePage
from config.config import BASE_URL
from pages.home_page import HomePage
from pages.Widgets.widget_menu_page import Widget_Page


def test_auto_complete(driver):

    driver.get(BASE_URL)

    home = HomePage(driver)
    home.open_home_page(BASE_URL)

    #WIDGET PAGE
    widget_menu_page = Widget_Page(driver)
    widget_menu_page.remove_ads()
    widget_menu_page.open_widgets()

    autocomplete = AutoCompletePage(driver)
    autocomplete.click_auto_menu()
    autocomplete.enter_multiple_colors(["Red", "Green" , "Yellow"])
    selected = autocomplete.get_selected_colors()
    expected = ["Red","Green","Yellow"]
    assert selected == expected

    autocomplete.enter_single_color("Red")
    selected = autocomplete.get_single_color()
    assert selected == "Red"





