from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class TensorHomePage(BasePage):
    """Содержит локаторы и действия на домашней странице tensor.ru"""
    P_POW_PEOPLE = By.XPATH, "//p[text()='Сила в людях']"
    ABOUT = By.XPATH, "//a[@href='/about' and contains(@class, 'tensor_ru-Index__link')]"

    def __init__(self, driver):
        super().__init__(driver)

    def click_about_in_p_pow_people(self):
        self.do_click(self.ABOUT)

    def p_pow_people_is_visible(self):
        return self.is_visible(self.P_POW_PEOPLE)

    def scroll_to_p_pow_people(self):
        self.scroll_to_element(self.P_POW_PEOPLE)

