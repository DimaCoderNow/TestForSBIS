import re

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class DownloadPage(BasePage):
    PLUGIN_BUTTON = By.XPATH, "//div[@class='controls-TabButton__caption' and text()='СБИС Плагин']"
    PLUGIN_LINK = By.XPATH, "//a[@href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']"
    PLUGIN_PATH = "Tests/sbisplugin-setup-web.exe"

    def click_plugin_button(self):
        element = self.get_element(self.PLUGIN_BUTTON)
        self.click_with_action(element)

    def download_plugin(self):
        return self.download_file(self.PLUGIN_LINK, self.PLUGIN_PATH)

    def get_size_file_in_site(self):
        text = self.get_element_text(self.PLUGIN_LINK)

        match = re.search(r'\d+\.\d+', text)
        if match:
            size_str = match.group()
            size_float = float(size_str)
            return size_float




