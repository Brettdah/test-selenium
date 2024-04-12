"""Module providing test fonctions to upload a file in different scenario."""

from page_objects.shop_page import ShopPage
from seleniumbase.common.exceptions import NoSuchElementException


class UploadTest(ShopPage):

    """Class to use for the upload manipulation"""

    def test_search_products(self):

        """Test the prodect search"""
        self.open_page()

        # Search the Toys
        self.send_keys(self.search_input, "Sunglasses")
        self.click(self.search_btn)

        # Assert product image
        try:
            self.assert_element(self.product_img)
            print("Yeah!! Found IT !!")
        except NoSuchElementException:
            print("Oh, NOOO !!! No more sunglasses")
            no_more_txt = "No products were found matching your selection."
            self.assert_text(no_more_txt, self.no_product_txt)
