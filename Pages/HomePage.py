from Config.config import TestData
from Pages.BasePage import BasePage

from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """Содержит локаторы домашней страницы sbis.ru"""
    CONTACTS = By.XPATH, "//a[@href='/contacts' and contains(@class, 'sbisru-Header__menu-link')]"
    DOWNLOAD_LINK = By.XPATH, "//a[@href='/download?tab=ereport&innerTab=ereport25' and @class='sbisru-Footer__link']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def click_contact(self):
        self.do_click(self.CONTACTS)

    def click_download_link(self):
        self.scroll_to_element(self.DOWNLOAD_LINK)
        self.do_click(self.DOWNLOAD_LINK)
