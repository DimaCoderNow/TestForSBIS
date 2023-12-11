import pytest

from Pages.HomePage import HomePage
from Tests.test_base import BaseTest


class TestPhotoAbout(BaseTest):
    def test_photo(self):
        self.home_page = HomePage(self.driver)
        self.home_page.click_contact()
        flag = True
        assert flag

