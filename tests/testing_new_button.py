import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from app_logics.find_in_comments_list import FindInCommentsList


class TestNewButton(unittest.TestCase):
    def setUp(self):
        self.test_comment = "First test comment"
        self.driver = webdriver.Chrome(
            executable_path="chromedriver.exe")
        self.driver.get("http://commentssprintone.azurewebsites.net")

    def test_adding_to_comments_list(self):
        push_the_button_new = self.driver.find_element_by_id("newbutton").click()
        make_new_comment = self.driver.find_element_by_id("Text")
        make_new_comment.send_keys(self.test_comment, Keys.ENTER)
        add_all_categories = self.driver.find_element_by_name("AllSelect")
        add_all_categories.send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(
            '//*[@id="editor-navigation"]/input[2]').click()
        find_result = FindInCommentsList(self.driver)
        self.assertIn(self.test_comment, find_result.search_in_list_by_comment())
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
