from lib.pages.base_page import BasePage
from lib.locators.login_page_locators import LOGIN_PAGE_LOCATORS as locator

class LoginPage(BasePage):
    def  __init__(self, driver):
        super().__init__(driver)

    def login(self,email,password):
        self.enter_text(locator.EMAIL_LOGIN_BOX,email)
        self.enter_text(locator.PASSWORD_BOX,password)
        self.click(locator.LOGIN_BUTTON)
