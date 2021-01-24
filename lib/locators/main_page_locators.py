from selenium.webdriver.common.by import By

class MAIN_PAGE_LOCATORS(object):
    USER_ACCOUNT_BUTTON = (By.CSS_SELECTOR,".link.account-user")
    LOGIN_BUTTON = (By.CSS_SELECTOR,".login-button")
    BOUTIQUE_LIST = (By.CSS_SELECTOR, ".component-list.component-big-list")
    BOUTIQUE_LIST_ITEM = (By.CSS_SELECTOR, ".component-item")
    BOUTIQUE_ITEM_IMAGE_CONTAINER = (By.CSS_SELECTOR, ".image-container")
    BOUTIQUE_ITEM_IMAGE = (By.TAG_NAME, "img")
    BOUTIQUE_TABS = (By.CSS_SELECTOR,".tab-link")
