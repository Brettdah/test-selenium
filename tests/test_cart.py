"""Module providing test fonctions for the cart."""

# import time
from selenium.webdriver.common.keys import Keys

from page_objects.cart_page import CartPage


class CartTest(CartPage):

    """Class to manipulate the cart"""

#    def setUp(self):
    def setUp(self):
        """Function to setUp"""
        super().setUp()
        print("opening cart")
        self.open_shop_page()

    def test_add2cart(self):
        """Function to test the cart"""
        # Add item to the cart
        self.click(self.converse_add_to_cart_btn)

        # Assert product is added
        self.assert_text("1", self.cart_count_txt)

        # Go to cart
        self.open_page()

        # get total
        price_before = self.get_text(self.subtotal_txt)

        # change Qty
        self.set_value(self.product_qty_input, "2")
        self.send_keys(self.product_qty_input, Keys.RETURN)

        # Wait few second
        # BAD PRACTICE
        # time.sleep(10)

        # Wait for loading to be completed
        # Not working
        # self.wait_for_element_visible(self.loading_overlay)
        # self.wait_for_element_not_visible(self.loading_overlay)

        # Wait for updated cart text instead
        self.wait_for_element_visible(self.updated_cart_txt)

        # Assert total to be different from last check
        self.assert_not_equal(price_before, self.get_text(self.subtotal_txt))
