from lib.pages.base_page import BasePage
from lib.locators.product_page_locators import PRODUCT_PAGE_LOCATORS as locator

class ProductPage(BasePage):
    def  __init__(self, driver):
        super().__init__(driver)

    def add_to_chart(self):
        self.click(locator.ADD_TO_BIN_BUTTON)
        return self.is_visible(locator.ADD_TO_BIN_BUTTON_TEXT)