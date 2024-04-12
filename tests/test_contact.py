"""
    Module providing test fonctions to use a contact form
    and by extention every form.
"""

from page_objects.contact_page import ContactPage


class ContactTest(ContactPage):

    """Class to use for the form manipulation"""

    def test_contact_page(self):
        """Function to fill and send the form"""
        # open the page
        self.open("https://practice.sdetunicorns.com/contact")
        # Or open home click on list contact
        # "id=menu-item-493"
        # fill in all the fields
        self.send_keys('.contact-name input', 'Mandalor')
        self.send_keys('.contact-email input', 'mandalor@mandayaim.org')
        self.send_keys('.contact-phone input', '0123456789')
        self.send_keys('.contact-message textarea', 'this is a test')

        # click the submit button
        self.click("#evf-submit-277")

        # verify submit message
        self.assert_text(
            "Thanks for contacting us! We will be in touch with you shortly",
            "div[role=alert]"
        )
