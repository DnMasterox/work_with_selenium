__author__ = 'nshumakov'

from selenium import webdriver
from app_logics.find_in_comments_list import FindInCommentsList
from app_logics.create_new_comment import search_in_list_by_comment
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.test_string = "Test string"
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.get("http://commentssprintone.azurewebsites.net")

    def test_untitled_test_case(self):
        driver = self.driver
        if search_in_list_by_comment(driver, self.test_string):
            driver.find_element_by_xpath("//*[@id='main']/div/div[5]"
                                         "/form/table/thead/tr/th[2]/a").click()
            driver.find_element_by_name("SelectedId").click()
            driver.find_element_by_xpath("//input[@value='Delete']").click()
            driver.find_element_by_xpath("//button/span").click()
        else:
            print("Something going wrong")
        find_result = FindInCommentsList(driver)
        self.assertNotIn(self.test_string, find_result.search_in_list_by_comment())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
