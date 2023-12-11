from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    """Содержит локаторы домашней страницы sbis.ru"""
    CONTACTS = By.XPATH, "//a[@href='/contacts' and contains(@class, 'sbisru-Header__menu-link')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def click_contact(self):
        self.do_click(self.CONTACTS)
