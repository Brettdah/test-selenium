"""Cart page descriptor"""

from seleniumbase import BaseCase


class CartPage(BaseCase):
    """Class to decribe the cart page"""
    converse_add_to_cart_btn = "a[aria-label='Add to cart: “Branded Converse”']"
    cart_count_txt = ".zak-header-col--2 span[class='count']"
    subtotal_txt = "td[class='product-subtotal']"
    product_qty_input = "input[id^='quantity']"
    update_cart_btn = "button[name='update_cart']"

    updated_cart_txt = ".woocommerce-message"
    # not working
    loading_overlay = ".woocommerce-cart-form div[class='blockOverlay']"

    def open_page(self):
        """open cart page"""
        self.open("https://practice.sdetunicorns.com/cart")

    def open_shop_page(self):
        """open shop page"""
        self.open("https://practice.sdetunicorns.com/shop")
