"""Shop page descriptor"""

from seleniumbase import BaseCase


class ShopPage(BaseCase):

    """Class to decribe the shop page"""
    search_input = "#woocommerce-product-search-field-0"
    search_btn = "button[value='Search']"
    product_img = ".woocommerce-product-gallery__image"
    no_product_txt = ".woocommerce-info"

    def open_page(self):

        """Open the shop page"""
        print("open shop page")
        self.open("https://practice.sdetunicorns.com/shop")
