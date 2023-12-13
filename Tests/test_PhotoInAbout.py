from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.HomePage import HomePage
from Pages.ContactsPage import ContactsPage
from Pages.TensorHomePage import TensorHomePage
from Pages.TensorAboutPage import TensorAboutPage


class TestPhotoAbout(BaseTest):

    def test_photo(self):
        self.my_logger.info("The photo test start")
        self.home_page = HomePage(self.driver)
        self.home_page.click_contact()

        self.contacts_page = ContactsPage(self.driver)
        self.contacts_page.click_banner_tensor()

        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])

        self.tensor_home_page = TensorHomePage(self.driver)

        self.my_logger.info(self.tensor_home_page.p_pow_people_is_visible())

        self.tensor_home_page.scroll_to_p_pow_people()
        self.tensor_home_page.click_about_in_p_pow_people()
        self.tensor_about_page = TensorAboutPage(self.driver)

        check_url = self.driver.current_url == TestData.ABOUT_TENSOR_URL
        self.my_logger.info(f"Check ABOUT_TENSOR_URL: {'OK'if check_url else 'FAILED'}")
        assert check_url, "URL check failed"

        self.tensor_about_page.work_header_is_visible()
        self.tensor_about_page.scroll_to_work_header()

        flag = self.compare_size_photo()

        if flag:
            self.my_logger.info("The photo test completed successfully")
        else:
            self.my_logger.info("The photo test failed")
        assert flag

    def compare_size_photo(self):
        sizes_photo_list = self.tensor_about_page.get_size_photo_in_work_block()
        for i in range(len(sizes_photo_list) - 1):
            if sizes_photo_list[i] != sizes_photo_list[i + 1]:
                return False
        return True

