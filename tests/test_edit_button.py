__author__ = 'nshumakov'

from selenium import webdriver
from app_logics.find_in_comments_list import FindInCommentsList
import unittest


class EditButtonTestCase(unittest.TestCase):
    def setUp(self):
        self.test_string = "Test string"
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get("http://commentssprintone.azurewebsites.net")

    def test_untitled_test_case(self):
        driver = self.driver
        driver.find_element_by_name("SelectedId").click()
        driver.find_element_by_xpath(
            "//*[@id='command-navigation']/input[2]").click()
        driver.find_element_by_id("Text").clear()
        driver.find_element_by_id("Text").send_keys(self.test_string)
        driver.find_element_by_xpath("//input[@value='Save & Return']").click()
        driver.find_element_by_xpath("//*[@id='main']/div/div[5]"
                                     "/form/table/thead/tr/th[2]/a").click()
        find_result = FindInCommentsList(self.driver)
        self.assertIn(self.test_string, find_result.search_in_list_by_comment())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
