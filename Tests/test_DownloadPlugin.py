import time

from selenium.webdriver import ActionChains

from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.HomePage import HomePage
from Pages.DownloadPage import DownloadPage
from Pages.TensorHomePage import TensorHomePage
from Pages.TensorAboutPage import TensorAboutPage


class TestDownloadPlugin(BaseTest):

    def test_plugin_download(self):
        self.my_logger.info("*****The plugin download test start*****")

        self.home_page = HomePage(self.driver)
        self.home_page.click_download_link()

        self.download_page = DownloadPage(self.driver)
        self.download_page.click_plugin_button()
        _, size_file = self.download_page.download_plugin()
        size_in_site = self.download_page.get_size_file_in_site()
        self.my_logger.info(f"Size in site: {size_in_site}")
        self.my_logger.info(f"Size file: {size_file}")
        check_equal_size = size_file == size_in_site
        self.my_logger.info(f"Check size equal: {'OK' if check_equal_size else 'FAILED'}")

        assert check_equal_size, "Check size equal FAILED"
        self.my_logger.info("The plugin download test successfully")
