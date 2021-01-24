from selenium.webdriver.common.by import By


class BOUTIQUE_PAGE_LOCATORS(object):
    PRODUCT_LIST = (By.CSS_SELECTOR,".products")
    PRODUCT_LIST_ITEM = (By.CSS_SELECTOR,".boutique-product")
    PRODUCT_ITEM_IMAGE_CONTAINER = (By.CSS_SELECTOR,".image-container")
    PRODUCT_ITEM_IMAGE= (By.TAG_NAME,"img")
