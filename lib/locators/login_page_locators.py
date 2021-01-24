from selenium.webdriver.common.by import By


class LOGIN_PAGE_LOCATORS(object):
    EMAIL_LOGIN_BOX=(By.ID,"login-email")
    PASSWORD_BOX = (By.ID,"login-password-input")
    LOGIN_BUTTON = (By.XPATH,"//button[@type='submit']")
