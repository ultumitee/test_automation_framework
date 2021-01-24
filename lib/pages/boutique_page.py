from random import randrange

from lib.pages.base_page import BasePage
from lib.locators.boutique_page_locators import BOUTIQUE_PAGE_LOCATORS as locator

class BoutiquePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        product_item_container=self.find_element(locator.PRODUCT_LIST)
        self.product_item_list=self.find_elements_of_element(product_item_container,locator.PRODUCT_LIST_ITEM)

    def check_if_product_images_loaded(self):
        for product_item in self.product_item_list:
            product_item_image_containers=self.find_elements_of_element(product_item,locator.PRODUCT_ITEM_IMAGE_CONTAINER)
            product_item_images=self.find_elements_of_element(product_item_image_containers[0],locator.PRODUCT_ITEM_IMAGE)
            if len(product_item_image_containers) == 0 or len(product_item_images) == 0 :
                return False
        return True

    def go_to_random_product(self):
        random_product_number = randrange(len(self.product_item_list))
        self.product_item_list[random_product_number].click()