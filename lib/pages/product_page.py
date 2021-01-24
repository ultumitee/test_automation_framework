from lib.pages.base_page import BasePage
from lib.locators.product_page_locators import PRODUCT_PAGE_LOCATORS as locator

class ProductPage(BasePage):
    def  __init__(self, driver):
        super().__init__(driver)
        print("Opened the Product page")
    def is_page_open(self):
        return self.is_visible_in_time(locator.ADD_TO_BIN_BUTTON,10)

    def add_to_chart(self):
        print("Adding item to basket")
        self.click(locator.ADD_TO_BIN_BUTTON)
        product_add_result=self.is_visible(locator.ADD_TO_BIN_BUTTON_TEXT)
        print("Product is added to basket -> {}".format(product_add_result))
        return product_add_result