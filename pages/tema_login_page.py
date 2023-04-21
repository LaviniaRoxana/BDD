"""
b. Login page https://the-internet.herokuapp.com/login
- Sa contina user, pass, login_btn si metode pt interactiune cu ele
"""

from selenium.webdriver.common.by import By

from browser import Browser


class LoginPage(Browser):


    USER_INPUT = (By.ID,"username")
    PASSWORD_INPUT = (By.ID,"password")
    LOGIN_BUTTON = (By.XPATH,"//html/body/div[2]/div/div/form/button/i")



    def navigate_to_login_page(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def set_email(self, email):
        self.driver.find_element(*self.USER_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()


LoginPage.navigate_to_login_page(LoginPage())
LoginPage.set_email(LoginPage(), "tomsmith")
LoginPage.set_password(LoginPage(), "SuperSecretPassword!")
LoginPage.click_login_button(LoginPage())




