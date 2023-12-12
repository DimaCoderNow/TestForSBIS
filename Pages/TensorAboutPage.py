from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class TensorAboutPage(BasePage):
    """Содержит локаторы и действия на странице tensor.ru/about"""
    WORK_HEADER = By.XPATH, "//h2[text()='Работаем']"
    PHOTO_IN_WORK_BLOCK = By.CLASS_NAME, "tensor_ru-About__block3-image"

    def __init__(self, driver):
        super().__init__(driver)

    def work_header_is_visible(self):
        self.is_visible(self.WORK_HEADER)

    def get_size_photo_in_work_block(self):
        list_sizes = []
        for photo in self.get_elements(self.PHOTO_IN_WORK_BLOCK):
            list_sizes.append(photo.size)
        return list_sizes

    def scroll_to_work_header(self):
        self.scroll_to_element(self.WORK_HEADER)

