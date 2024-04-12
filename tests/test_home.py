"""Module providing test fonctions to check things on a web page."""

from page_objects.home_page import HomePage
from page_objects.my_account_page import MyAccountPage as account


class HomeTest(HomePage):

    """Class to use to check the home page"""

    def setUp(self):
        """Function to setUp"""
        super().setUp()
        print("Openning the home page")
        # Open home page and go on to login
        self.open_page()
        print("click on login")
        self.click(self.menu_login)
        print("OPT IN")
        # account.login(account)
        self.add_text(account.txt_area_user_selector, "testuser")
        self.add_text(account.txt_area_password_selector, "PracticeSite123!!")
        self.click(account.button_login)
        self.assert_text("Log out", account.logout_txt_selector)

        # Open home page
        self.open_page()

    def tearDown(self):
        """Function to teardown"""
        print("logging Out")
        self.click(self.menu_login)
        self.click(account.logout_link)
        self.assert_element_visible(account.button_login)

        super().tearDown()

    def test_home_page(self):

        """Function to assert some things on the home page"""

        # assert page tittle
        self.assert_title("Practice E-Commerce Site – SDET Unicorns")

        # asster logo
        self.assert_element(self.logo_img_selector)

        # Click on the get started button and assert url
        # '#get-started
        self.click(self.get_started_button)
        # self.assert_equal(
        #     self.get_current_url(),
        #     "https://practice.sdetunicorns.com/#get-started"
        # )
        self.assert_true("get-started" in self.get_current_url())
        # get the text of the header and assert the value
        heading_txt = "Think different. Make different."
        self.assert_text(heading_txt, self.heading_selector)
        # Exercise
        self.scroll_to_bottom()
        copyright_txt = "Copyright © 2020 SDET Unicorns"
        self.assert_text(copyright_txt, self.copyright_selector)

    def test_menu_links(self):

        """Function to assert menu is not tempered"""

        expected_links = [
            'Home',
            'About',
            'Shop',
            'Blog',
            'Contact',
            'My account'
        ]

        # Open home page
        # self.open("https://practice.sdetunicorns.com")

        # find menu links elements
        myselector = self.find_elements(self.menu_link_selector)
        for idx, link_elm in enumerate(myselector):
            self.assertEqual(expected_links[idx], link_elm.text)
