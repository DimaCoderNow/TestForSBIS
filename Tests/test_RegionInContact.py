from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.HomePage import HomePage
from Pages.ContactsPage import ContactsPage


class TestRegionContact(BaseTest):

    def test_region_contact(self):
        self.my_logger.info("*****The region in contact test start*****")
        # Переходим на sbis.ru
        self.home_page = HomePage(self.driver)
        # Переходим в раздел контакты
        self.home_page.click_contact()

        self.contacts_page = ContactsPage(self.driver)
        # Проверяем что мой регион определился верно
        check_my_region = self.contacts_page.current_region() == TestData.MY_REGION
        self.my_logger.info(f"Check my region: {'OK' if check_my_region else 'FAILED'}")
        assert check_my_region, f"Check my region failed"
        # Проверяем что есть список партнеров
        check_partners = self.contacts_page.region_partners_is_visible()
        self.my_logger.info(f"Partners is visible: {'OK' if check_partners else 'FAILED'}")
        assert check_partners, "Partners not is visible"
        # Сохраняем первого партнера, что бы проверить изменения
        first_partner = self.contacts_page.get_first_partner()
        # Сохраняем URL, что бы проверить изменения
        url = self.driver.current_url
        # меняем регион, регион задается в config.py
        self.contacts_page.change_region()
        # Получаем текущий регион и проверяем что он соответствует новому региону
        check_region_changed = self.contacts_page.current_region() == TestData.CHANGE_REGION
        self.my_logger.info(f"Region is changed : {'OK' if check_region_changed else 'FAILED'}")
        assert check_region_changed, "Check region is changed failed "
        # Проверяем что партнеры изменились
        check_different_partners = first_partner != self.contacts_page.get_first_partner()
        self.my_logger.info(f"Partners is different: {'OK' if check_different_partners else 'FAILED'}")
        # Проверяем что URL изменился
        check_different_url = url != self.driver.current_url
        self.my_logger.info(f"URL is different: {'OK' if check_different_url else 'FAILED'}")
        # Проверяем что title содержит информацию выбранного региона
        check_title = TestData.CHANGE_REGION in self.driver.title
        self.my_logger.info(f"Title contains new region: {'OK' if check_title else 'FAILED'}")

        assert check_title, "Title not contains new region"
        assert check_different_url, "URL not different"
        assert check_different_partners, "Partners not different"

        self.my_logger.info("The region in contact test successfully")

