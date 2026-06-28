from pages.frame.Modal_Dialogs_Page import ModalDialogsPage
from config.config import BASE_URL
from pages.home_page import HomePage
from pages.alert_frame_windows import AlertFrameWindows



def test_alert_cancel(driver):
    driver.get(BASE_URL)
    #home
    home = HomePage(driver)
    home.open_home_page(BASE_URL)

    #Alert,Frame & Windows
    afw = AlertFrameWindows(driver)
    afw.click_alert_frame_window()


    #Modal Dialogs
    modal_dialog = ModalDialogsPage(driver)
    modal_dialog.click_modal_dialog_menu()

    # Remove DemoQA advertisement
    modal_dialog.remove_ads()
    modal_dialog.click_large_modal_button()

    #Get the text
    text = modal_dialog.get_large_modal_text()
    #assertion
    assert "lorem ipsum is simply" in text.lower()

    modal_dialog.click_large_close_button()



