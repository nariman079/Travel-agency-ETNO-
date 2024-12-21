import unittest
import time

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TourE2ETests(unittest.TestCase):
    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def tearDown(self):
        self.driver.quit()

    def test_template_1_buttons(self):
        self.driver.get("http://localhost:8080/")
        self.assertIn('Главная страницы', self.driver.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
