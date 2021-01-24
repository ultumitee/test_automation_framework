import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage(object):
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver ):
        self.driver = driver
        self.timeout = 30
        self.driver.implicitly_wait(self.timeout)

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def find_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return self.driver.find_element(*by_locator)

    def get_text_of_element(self,by_locator):
        return self.find_element(by_locator).text

    def timer_click(self, by_locator, timer):
        WebDriverWait(self.driver, timer).until(EC.element_to_be_clickable(by_locator)).click()
    # End Of Definition
    def wait_until_invisibility_of_element(self,by_locator,timer):
        element = WebDriverWait(self.driver, timer).until(EC.invisibility_of_element(by_locator))
        return bool(element)

    def is_visible_in_time(self, by_locator,timer):
        element = WebDriverWait(self.driver, timer).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    def scroll_down(self):
        self.driver.execute_java_script("window.scrollTo(0,document.body.scrollHeight/3)")

    def find_elements(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(by_locator))
        return self.driver.find_elements(*by_locator)

    def find_element_of_element(self,element,by_locator):
        return element.find_element(*by_locator)

    def find_elements_of_element(self,element,by_locator):
        return element.find_elements(*by_locator)

    def scroll_page_from_element(self,direction,locator):
        self.click(locator)
        if direction.lower()=="up":
            self.find_element(locator).send_keys(Keys.PAGE_UP)
        elif direction.lower()=="down":
            self.find_element(locator).send_keys(Keys.PAGE_DOWN)
        elif direction.lower()=="right":
            self.find_element(locator).send_keys(Keys.RIGHT)
        elif direction.lower()=="left":
            self.find_element(locator).send_keys(Keys.LEFT)
        else:
            print("wrong direction")

    def get_url_of_page(self):
        return self.driver.current_url

    def scroll_to_element(self,by_locator):
        element=self.find_element(by_locator)
        actions=ActionChains(self.driver)
        actions.move_to_element(element).perform()
