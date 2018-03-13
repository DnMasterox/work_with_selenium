import os
import unittest

from selenium import webdriver
from app_logics.comments_list import CommentsList
from app_logics.preparing_for_buttons_tests import \
    create_new_comment_save, \
    create_new_comment_save_return, prepare_duplicate_button_for_test, \
    prepare_edit_button_for_test, prepare_delete_button_for_tests


class TestPages(unittest.TestCase):
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

    def test_new_comments_page_first(self):
        create_new_comment_save(self.driver, self.test_comment_one,
                                self.number_for_test_comment_one)
        comments_list = CommentsList(self.driver)
        self.assertIn(self.number_for_test_comment_one,
                      comments_list.search_by_number())

    def test_new_comments_page__second(self):
        create_new_comment_save_return(self.driver, self.test_comment_two)
        find_result = CommentsList(self.driver)
        self.assertIn(self.test_comment_two,
                      find_result.search_by_comment())

    def test_duplicate_button(self):
        prepare_duplicate_button_for_test(self.driver, self.test_comment_three)
        find_result = CommentsList(self.driver)
        self.assertIn(self.test_comment_three,
                      find_result.search_by_comment())

    def test_edit_button(self):
        prepare_edit_button_for_test(self.driver, self.test_comment_four)
        find_result = CommentsList(self.driver)
        self.assertIn(self.test_comment_four,
                      find_result.search_by_comment())

    def test_delete_button(self):
        create_new_comment_save_return(self.driver, self.test_comment_five)
        prepare_delete_button_for_tests(self.driver)
        find_result = CommentsList(self.driver)
        self.assertNotIn(self.test_comment_five,
                         find_result.search_by_comment())

    if __name__ == '__main__':
        unittest.main()
