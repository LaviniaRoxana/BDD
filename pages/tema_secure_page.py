"""
c. Secure page https://the-internet.herokuapp.com/secure
- Sa contina mesajul de succes si verificare ca e displayed
- Sa contina logout_btn si click pe el
"""

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser
from pages.tema_login_page import LoginPage


class SecurePage(Browser):
    LOGOUT_BUTTON = (By.XPATH, "/html/body/div[2]/div/div/a/i")
    MESAJ_SUCCES = (By.ID, "flash")

    def navigate_to_secure_page(self):
        self.driver.get("https://the-internet.herokuapp.com/secure")

    def verify_mesaj_succes(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.MESAJ_SUCCES).text
        except NoSuchElementException:
            actual_message = "None"

        assert actual_message == expected_message, f"Error, the message is incorrect, actual message"

    def verify_mesaj_displayed(self):
        mesaj_displayed = self.driver.find_element(*self.MESAJ_SUCCES)
        assert mesaj_displayed.is_displayed() == True, f"mesajul nu apare"

    def click_logout_button(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()


SecurePage.verify_mesaj_succes(SecurePage(), 'You logged into a secure area!\n×')
SecurePage.verify_mesaj_displayed(SecurePage())
SecurePage.click_logout_button(SecurePage())
