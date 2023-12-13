import os
import time
import requests

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Данный класс является родителем всех страниц и содержит базовые методы"""

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        time.sleep(2)
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).click()

    def get_element_text(self, by_locator):
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def is_visible(self, by_locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False

    def get_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        return elements

    def is_visible_elements(self, by_locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(by_locator))
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.location_once_scrolled_into_view
        time.sleep(2)

    def click_with_action(self, element):
        time.sleep(1)
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.click()
        action.perform()

    def download_file(self, by_locator, download_path):
        """Возвращает путь к скаченному файлу и его размер в Mb"""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

        file_url = element.get_attribute("href")
        response = requests.get(file_url)

        if response.status_code == 200:
            with open(download_path, 'wb') as file:
                file.write(response.content)
            file_size = round(os.path.getsize(download_path)/(1024.0 ** 2), 2)
            return download_path, file_size
        return None, None

    def next_window_handles(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
