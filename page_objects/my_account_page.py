"""My account page descriptor"""

from seleniumbase import BaseCase


class MyAccountPage(BaseCase):

    """Class to decribe the account page"""

    txt_area_user_selector = "#username"
    txt_area_password_selector = "#password"
    button_login = "button[name=login]"
    logout_txt_selector = ".woocommerce-MyAccount-content"
    logout_link = ".woocommerce-MyAccount-content a[href*=logout]"
