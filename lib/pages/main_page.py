from lib.pages.base_page import BasePage
from lib.locators.main_page_locators import MAIN_PAGE_LOCATORS as locator
from random import randrange
class MainPage(BasePage):
    def  __init__(self, driver):
        super().__init__(driver)
        self.boutique_tabs=self.find_elements(locator.BOUTIQUE_TABS)
    def go_to_login(self):
        self.click(locator.USER_ACCOUNT_BUTTON)
        self.click(locator.LOGIN_BUTTON)

    def get_tab_count(self):
        return len(self.boutique_tabs)

    def switch_to_tab(self,index):
        tab_to_switch = self.boutique_tabs[index]
        tab_to_switch.click()
        boutique_container = self.find_element(locator.BOUTIQUE_LIST)
        self.boutique_list= self.find_elements_of_element(boutique_container,locator.BOUTIQUE_LIST_ITEM)

    def check_if_boutique_images_loaded(self):
        for boutique_item in self.boutique_list:
            boutique_item_image_containers=self.find_elements_of_element(boutique_item,locator.BOUTIQUE_ITEM_IMAGE_CONTAINER)
            boutique_item_images=self.find_elements_of_element(boutique_item_image_containers[0],locator.BOUTIQUE_ITEM_IMAGE)
            if len(boutique_item_image_containers) == 0 or len(boutique_item_images) == 0 :
                return False
        return True

    def go_to_random_boutique(self):
        random_tab_number=randrange(len(self.boutique_tabs))
        self.switch_to_tab(random_tab_number)
        boutique_number=len(self.boutique_list)
        random_boutique_number = randrange(boutique_number)
        self.boutique_list[random_boutique_number].click()
