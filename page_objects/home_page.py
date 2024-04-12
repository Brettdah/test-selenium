"""home page descriptor"""

from seleniumbase import BaseCase


class HomePage(BaseCase):

    """Class to decribe the Home page"""

    logo_img_selector = ".custom-logo-link"
    get_started_button = "#get-started"
    heading_selector = "h1"
    copyright_selector = ".zak-footer-bar__1"
    menu_link_selector = "//ul[@id='zak-primary-menu']  //*[starts-with(@id,'menu-item')]"
    menu_login = "#menu-item-619 a[href*=my-account]"
    txt_area_user_selector = "#username"
    txt_area_password_selector = "#password"
    button_login = "button[name=login]"

    def open_page(self):
        """open home page"""
        # Open home page
        self.open("https://practice.sdetunicorns.com")

    def login(self):
        """login on the account page"""
        self.add_text(self.txt_area_user_selector, "testuser")
        self.add_text(self.txt_area_password_selector, "PracticeSite123!!")
        self.click(self.button_login)
