"""
a. Home page https://the-internet.herokuapp.com/
- Sa aiba cel putin 3 elemente inlcusiv Form Authentication
- Sa contina metode de click pe ele
"""


from selenium.webdriver.common.by import By

from browser import Browser

class HomePage(Browser):

    CHECKBOXES = (By.XPATH, "/html/body/div[2]/div/ul/li[6]/a")
    DRAG_AND_DROP = (By.XPATH, "/html/body/div[2]/div/ul/li[10]/a")
    FORM_AUTHENTICATION = (By.XPATH, "/html/body/div[2]/div/ul/li[21]/a")

    def navigate_to_home_page(self):
        self.driver.get("https://the-internet.herokuapp.com/")

    def click_checkboxes_button(self):
        self.driver.find_element(*self.CHECKBOXES).click()

    def click_DRAG_AND_DROP_button(self):
        self.driver.find_element(*self.DRAG_AND_DROP).click()

    def click_FORM_AUTHENTICATION_button(self):
        self.driver.find_element(*self.FORM_AUTHENTICATION).click()

HomePage.navigate_to_home_page(HomePage())
HomePage.click_checkboxes_button(HomePage())
HomePage.navigate_to_home_page(HomePage())
HomePage.click_DRAG_AND_DROP_button(HomePage())
HomePage.navigate_to_home_page(HomePage())
HomePage.click_FORM_AUTHENTICATION_button(HomePage())


