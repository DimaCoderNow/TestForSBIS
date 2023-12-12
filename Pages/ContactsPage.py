from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ContactsPage(BasePage):
    """Содержит локаторы и действия на страницы контакты sbis.ru"""
    BANNER_TENSOR = By.XPATH, "//a[@title='tensor.ru' and contains(@class,'mb-12')]"

    def __init__(self, driver):
        super().__init__(driver)

    def click_banner_tensor(self):
        self.do_click(self.BANNER_TENSOR)

