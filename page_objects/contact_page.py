"""Contact page descriptor"""

from seleniumbase import BaseCase


class ContactPage(BaseCase):

    """Class to decribe the contact page"""

    contact_name_selector = ".contact-name input"
    contact_mail_selector = ".contact-email input'"
    contact_phone_selector = ".contact-phone input"
    contact_message_selector = ".contact-message textarea"

    contact_submit_btn_selector = "#evf-submit-277"

    contact_submit_message_txt_selector = "div[role=alert]"

    def open_page(self):
        """Open the contact page page"""
        self.open("https://practice.sdetunicorns.com/contact")
