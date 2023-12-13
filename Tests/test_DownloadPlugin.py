from Tests.test_base import BaseTest
from Pages.HomePage import HomePage
from Pages.DownloadPage import DownloadPage


class TestDownloadPlugin(BaseTest):

    def test_plugin_download(self):
        self.my_logger.info("*****The plugin download test start*****")
        # Переходим на sbis.ru и в Footer'e кликаем на Скачать СБИС
        self.home_page = HomePage(self.driver)
        self.home_page.click_download_link()
        # Получаем объект страницы загрузок
        self.download_page = DownloadPage(self.driver)
        # Выбираем СБИС Плагин
        self.download_page.click_plugin_button()
        # Скачиваем файл и получаем его размер
        _, size_file = self.download_page.download_plugin()
        # Получаем размер указанный на сайте
        size_in_site = self.download_page.get_size_file_in_site()

        self.my_logger.info(f"Size in site: {size_in_site}" if size_in_site else "Get size in site FAILED")
        self.my_logger.info(f"Size downloaded file: {size_file}")
        # Сравниваем размеры скаченного файла и указанного на сайте
        check_equal_size = size_file == size_in_site
        self.my_logger.info(f"Check size equal: {'OK' if check_equal_size else 'FAILED'}")

        assert check_equal_size, "Check size equal FAILED"
        self.my_logger.info("The plugin download test successfully")
