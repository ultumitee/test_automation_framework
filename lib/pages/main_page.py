from lib.pages.base_page import BasePage
from lib.locators.main_page_locators import MAIN_PAGE_LOCATORS as locator
from random import randrange
class MainPage(BasePage):
    def  __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.trendyol.com/")
        self.click(locator.CLOSE_POP_UP_BUTTON)
        self.boutique_tabs=self.find_elements(locator.BOUTIQUE_TABS)
        print("Opened the main page")
    def is_page_open(self):
        return self.is_visible_in_time(locator.BOUTIQUE_LIST,10)

    def go_to_login(self):
        print("Going to login page")
        self.click(locator.USER_ACCOUNT_BUTTON)
        #self.click(locator.LOGIN_BUTTON)
    def user_logged_in(self):
        #my_account_button=self.find_elements(locator.MY_ACCOUNT_BUTTON)
        user_logged_in = self.is_visible_in_time(locator.MY_ACCOUNT_BUTTON,10)
        print("User Logged in -> {}".format(user_logged_in))
        print("Opened the Main Page")
        return user_logged_in
    def get_tab_count(self):
        print("There are {} TABs".format(len(self.boutique_tabs)))
        return len(self.boutique_tabs)

    def switch_to_tab(self,index):
        self.boutique_tabs=self.find_elements(locator.BOUTIQUE_TABS)
        tab_to_switch = self.boutique_tabs[index]
        print("Switching to TAB {}".format(index+1))
        tab_to_switch.click()
        boutique_container = self.find_element(locator.BOUTIQUE_LIST)
        self.boutique_list= self.find_elements_of_element(boutique_container,locator.BOUTIQUE_LIST_ITEM)

    def check_if_boutique_images_loaded(self):
        for boutique_item in self.boutique_list:
            boutique_item_image_containers=self.find_elements_of_element(boutique_item,locator.BOUTIQUE_ITEM_IMAGE_CONTAINER)
            boutique_item_images=self.find_elements_of_element(boutique_item_image_containers[0],locator.BOUTIQUE_ITEM_IMAGE)
            if len(boutique_item_image_containers) == 0 or len(boutique_item_images) == 0 :
                print("Boutique image is not loaded for {}".format(boutique_item.text))
                return False
        print("All boutique images are loaded successfully")
        return True

    def go_to_random_boutique(self):
        random_tab_number=randrange(len(self.boutique_tabs))
        print("Switching to a random boutique tab")
        self.switch_to_tab(random_tab_number)
        boutique_number=len(self.boutique_list)
        random_boutique_number = randrange(boutique_number)
        print("Navigating to a random boutique")
        self.boutique_list[random_boutique_number].click()
