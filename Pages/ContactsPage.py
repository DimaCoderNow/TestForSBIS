import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class ContactsPage(BasePage):
    """Содержит локаторы и действия на страницы контакты sbis.ru"""
    BANNER_TENSOR = By.XPATH, "//a[@title='tensor.ru' and contains(@class,'mb-12')]"
    REGION_CHOOSER = By.XPATH, "//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']"
    REGION_PARTNERS = By.XPATH, "//div[@class='sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis " \
                                "sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32']"
    NEW_REGION = By.XPATH, f"//span[@title='{TestData.CHANGE_REGION}' and @class='sbis_ru-link']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_banner_tensor(self):
        self.do_click(self.BANNER_TENSOR)

    def current_region(self):
        region = self.get_element_text(self.REGION_CHOOSER)
        return region

    def region_partners_is_visible(self):
        return self.is_visible_elements(self.REGION_PARTNERS)

    def change_region(self):
        self.do_click(self.REGION_CHOOSER)
        self.do_click(self.NEW_REGION)
        time.sleep(3)

    def get_first_partner(self):
        return self.get_element_text(self.REGION_PARTNERS)

