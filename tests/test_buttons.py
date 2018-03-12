import os
import unittest

from selenium import webdriver
from app_logics.find_in_comments_list import FindInCommentsList
from app_logics.preparing_for_buttons_tests import \
    prepare_new_button_for_first_test, \
    prepare_new_button_for_second_test, prepare_duplicate_button_for_test, \
    prepare_edit_button_for_test, prepare_delete_button_for_tests


class TestButtons(unittest.TestCase):
    def setUp(self):
        self.test_comment_one = "First test comment"
        self.number_for_test_comment_one = 888
        self.test_comment_two = "Second test comment"
        self.test_comment_three = "Third test comment"
        self.test_comment_four = "Fourth test comment"
        self.test_comment_five = "Fifth test comment"
        self.driver = webdriver.Chrome(
            executable_path=os.path.join(os.path.dirname(
                __file__), '..', 'drivers', 'chromedriver.exe'))
        self.driver.get("http://commentssprintone.azurewebsites.net")

    def tearDown(self):
        self.driver.quit()

    def test_new_button_first(self):
        driver = self.driver
        prepare_new_button_for_first_test(driver, self.test_comment_one,
                                          self.number_for_test_comment_one)
        find_result = FindInCommentsList(driver)
        self.assertIn(self.number_for_test_comment_one,
                      find_result.search_in_list_by_number())

    def test_new_button_second(self):
        driver = self.driver
        prepare_new_button_for_second_test(driver, self.test_comment_two)
        find_result = FindInCommentsList(driver)
        self.assertIn(self.test_comment_two,
                      find_result.search_in_list_by_comment())

    def test_duplicate_button(self):
        driver = self.driver
        prepare_duplicate_button_for_test(driver, self.test_comment_three)
        find_result = FindInCommentsList(driver)
        self.assertIn(self.test_comment_three,
                      find_result.search_in_list_by_comment())

    def test_edit_button(self):
        driver = self.driver
        prepare_edit_button_for_test(driver, self.test_comment_four)
        find_result = FindInCommentsList(self.driver)
        self.assertIn(self.test_comment_four,
                      find_result.search_in_list_by_comment())

    def test_delete_button(self):
        driver = self.driver
        prepare_new_button_for_second_test(driver, self.test_comment_five)
        prepare_delete_button_for_tests(driver)
        find_result = FindInCommentsList(driver)
        self.assertNotIn(self.test_comment_five,
                         find_result.search_in_list_by_comment())

    if __name__ == '__main__':
        unittest.main()
