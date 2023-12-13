import pytest
import logging
from selenium import webdriver


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    logger, handler = test_logging()
    request.cls.my_logger = logger
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
        web_driver.maximize_window()
        request.cls.driver = web_driver

        yield

        logger.removeHandler(handler)
        handler.close()

        web_driver.close()


def test_logging():
    log_path = "test.log"
    logger = logging.getLogger('selenium')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_path)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logging.getLogger('selenium.webdriver.common').setLevel(logging.INFO)

    return logger, handler
