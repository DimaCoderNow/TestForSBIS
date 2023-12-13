from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class DownloadPage(BasePage):
    PLUGIN_BUTTON = (By.XPATH, "//div[@class='controls-TabButton__caption' and text()='СБИС Плагин']")
    # PLUGIN_BUTTON = (By.XPATH, "//*[@id='ws-4gpt5we7nj91702419796079']/div[2]")

    def get_plugin_button(self):
        return self.get_element(self.PLUGIN_BUTTON)

