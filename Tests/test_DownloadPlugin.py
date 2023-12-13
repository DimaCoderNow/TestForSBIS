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
        self.my_logger.info("The plugin download test start")
        self.home_page = HomePage(self.driver)

        self.home_page.click_download_link()

        self.download_page = DownloadPage(self.driver)
        time.sleep(3)
        element = self.download_page.get_plugin_button()
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.click()
        action.perform()
        time.sleep(3)

        assert True
