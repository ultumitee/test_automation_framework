from lib.pages.main_page import MainPage
from lib.pages.boutique_page import BoutiquePage
from lib.pages.login_page import LoginPage
from lib.pages.product_page import ProductPage
class TestClass(object):
    def test_trendyol(self,browser,user_data):
        main_page=MainPage(browser) #User opens the trendyol main page
        assert main_page.is_page_open() #Verify if mainpage is open
        main_page.go_to_login() #User goes to login page
        login_page=LoginPage(browser)
        assert login_page.is_page_open() #Veriyf is login page is open
        login_page.login(user_data["EMAIL"],user_data["PASSWORD"])# user log in with credentials in user_info yaml file
        assert main_page.user_logged_in() #verify if log in is successful
        tab_count=main_page.get_tab_count() #get the number of tabs to iterate over
        for index in range(tab_count): #iterate over the tabs one by one
            main_page.switch_to_tab(index)
            main_page.check_if_boutique_images_loaded() # for each tabs, check if images are loaded
        main_page.go_to_random_boutique() #go to a random boutique
        boutique_page = BoutiquePage(browser)
        assert boutique_page.is_page_open() #verify if boutique page is open
        boutique_page.check_if_product_images_loaded() #check if product images are loaded
        boutique_page.go_to_random_product() #go to a random product
        product_page=ProductPage(browser)
        assert product_page.is_page_open() #verify if product page is open
        assert product_page.add_to_chart() #verify if add to chart operation is successful