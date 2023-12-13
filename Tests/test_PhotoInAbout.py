from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.HomePage import HomePage
from Pages.ContactsPage import ContactsPage
from Pages.TensorHomePage import TensorHomePage
from Pages.TensorAboutPage import TensorAboutPage


class TestPhotoAbout(BaseTest):

    def test_photo(self):
        self.my_logger.info("*****The size photo test start*****")
        # Переходим на sbis.ru
        self.home_page = HomePage(self.driver)
        # Переходим в раздел контакты
        self.home_page.click_contact()

        self.contacts_page = ContactsPage(self.driver)
        # Кликаем по баннеру ТЕНЗОР
        self.contacts_page.click_banner_tensor()

        # Переходим на следующую вкладку в браузере
        self.contacts_page.next_window_handles()

        self.tensor_home_page = TensorHomePage(self.driver)
        # Проверяем наличие блока "Сила в людях"
        check_block_power_people = self.tensor_home_page.p_pow_people_is_visible()
        self.my_logger.info(f"Block power people is visible: {'OK' if check_block_power_people else 'FAILED'}")
        # Переходим к блоку "Сила в людях"
        self.tensor_home_page.scroll_to_p_pow_people()
        # Кликаем по "Подробнее" в блоке "Сила в людях"
        self.tensor_home_page.click_about_in_p_pow_people()
        self.tensor_about_page = TensorAboutPage(self.driver)
        # Проверяем что текущий url соответствует url страницы about
        check_url = self.driver.current_url == TestData.ABOUT_TENSOR_URL
        self.my_logger.info(f"Check url about Tensor: {'OK'if check_url else 'FAILED'}")
        assert check_url, f"URL {TestData.ABOUT_TENSOR_URL} check failed"

        # Находим раздел "Работаем" и проверяем, что у всех фотографий хронологии одинаковые высота и ширина
        self.tensor_about_page.work_header_is_visible()
        self.tensor_about_page.scroll_to_work_header()

        flag = self.compare_size_photo()
        self.my_logger.info(f"Check size photo equal: {'OK' if flag else 'FAILED'}")

        assert flag, "The size photo test failed"

        self.my_logger.info("The size photo test completed successfully")

    def compare_size_photo(self):
        sizes_photo_list = self.tensor_about_page.get_size_photo_in_work_block()
        for i in range(len(sizes_photo_list) - 1):
            if sizes_photo_list[i] != sizes_photo_list[i + 1]:
                return False
        return True

