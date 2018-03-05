import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestAddingToCommentsList(unittest.TestCase):
    def setUp(self):
        self.test_comment = "First test comment"
        self.driver = webdriver.Chrome(
            executable_path="chromedriver.exe")
        self.driver.get("http://commentssprintone.azurewebsites.net")

    def test_adding_to_comments_list(self):
        push_the_button_new = self.driver.find_element_by_id("newbutton")
        push_the_button_new.send_keys(Keys.ENTER)
        make_new_comment = self.driver.find_element_by_id("Text")
        make_new_comment.send_keys(self.test_comment, Keys.ENTER)
        add_all_categories = self.driver.find_element_by_name("AllSelect")
        add_all_categories.send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="editor-navigation"]/input[2]').click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/form/table/thead/tr/th[2]/a').click()
        self.driver.find_element_by_xpath(''
                                          '//*[@id="main"]/div/div[5]/'
                                          'form/table/tbody/tr[1]'
                                          '/td[1]/input[1]').click()
        self.driver.find_element_by_xpath('//*[@id="command-navigation"]/input[2]').click()
        comparison_value_getting = self.driver.find_element_by_id("Text").get_attribute("value")
        self.assertEqual(comparison_value_getting, self.test_comment)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
