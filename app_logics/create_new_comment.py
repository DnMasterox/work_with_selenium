from selenium.webdriver.common.keys import Keys
from app_logics.find_in_comments_list import FindInCommentsList

__author__ = 'nshumakov'


def search_in_list_by_comment(web_driver, comment) -> bool:
    push_the_button_new = web_driver.find_element_by_id("newbutton").click()
    make_new_comment = web_driver.find_element_by_id("Text")
    make_new_comment.send_keys(comment, Keys.ENTER)
    add_all_categories = web_driver.find_element_by_name("AllSelect")
    add_all_categories.send_keys(Keys.ENTER)
    web_driver.find_element_by_xpath(
        '//*[@id="editor-navigation"]/input[2]').click()
    find_result = FindInCommentsList(web_driver)
    list_of_results = find_result.search_in_list_by_comment()
    for result in list_of_results:
        if comment in result:
            return True
        else:
            return False