from selenium.webdriver.common.keys import Keys

__author__ = 'nshumakov'

DIGIT_ONE = 1
DIGIT_TWO = 2
DIGIT_FIVE = 5


def prepare_new_button_for_first_test(driver, text_comment,
                                      number_comment) -> None:
    push_the_button_new = driver.find_element_by_id("newbutton")
    push_the_button_new.click()
    new_comment_text_add = driver.find_element_by_id("Text")
    new_comment_text_add.send_keys(text_comment)
    new_comment_number_add = driver.find_element_by_id("Number")
    new_comment_number_add.send_keys(number_comment)
    add_all_categories = driver.find_element_by_name("AllSelect")
    add_all_categories.send_keys(Keys.ENTER)
    save_button = driver.find_element_by_xpath(
        '//*[@id="editor-navigation"]/input[%d]' % DIGIT_ONE)
    save_button.click()
    return_button = driver.find_element_by_xpath(
        '//*[@id="logindisplay"]/a')
    return_button.click()


def prepare_new_button_for_second_test(driver, text_comment) -> None:
    push_the_button_new = driver.find_element_by_id("newbutton")
    push_the_button_new.click()
    make_new_comment = driver.find_element_by_id("Text")
    make_new_comment.send_keys(text_comment)
    add_all_categories = driver.find_element_by_name("AllSelect")
    add_all_categories.send_keys(Keys.ENTER)
    save_and_return_button = driver.find_element_by_xpath(
        '//*[@id="editor-navigation"]/input[%d]' % DIGIT_TWO)
    save_and_return_button.click()


def prepare_duplicate_button_for_test(driver, text_comment) -> None:
    select_comment_for_duplicate = driver.find_element_by_name(
        "SelectedId")
    select_comment_for_duplicate.click()
    button_duplicate = driver.find_element_by_xpath(
        "//input[@value='Duplicate...']")
    button_duplicate.click()
    text_field = driver.find_element_by_id("Text")
    text_field.clear()
    text_field.send_keys(text_comment)
    number_field = driver.find_element_by_id("Number")
    number_field.clear()
    save_and_return_button = driver.find_element_by_xpath(
        "//input[@value='Save & Return']")
    save_and_return_button.click()


def prepare_edit_button_for_test(driver, text_comment) -> None:
    select_comment_for_duplicate = driver.find_element_by_name(
        "SelectedId")
    select_comment_for_duplicate.click()
    driver.find_element_by_xpath(
        "//*[@id='command-navigation']/input[%d]" % DIGIT_TWO).click()
    text_field = driver.find_element_by_id("Text")
    text_field.clear()
    text_field.send_keys(text_comment)
    save_and_return_button = driver.find_element_by_xpath(
        "//input[@value='Save & Return']")
    save_and_return_button.click()
    refresh_comments_list = driver.find_element_by_xpath(
        "//*[@id='main']/div/div[%d]/form/table/thead/tr/th[%d]/a"
        % (DIGIT_FIVE, DIGIT_TWO))
    refresh_comments_list.click()


def prepare_delete_button_for_tests(driver) -> None:
    refresh_comments_list = driver.find_element_by_xpath(
        "//*[@id='main']/div/div[%d]/form/table/thead/tr/th[%d]/a" % (DIGIT_FIVE, DIGIT_TWO))
    refresh_comments_list.click()
    select_comment_for_deleting = driver.find_element_by_name(
        "SelectedId")
    select_comment_for_deleting.click()
    button_delete = driver.find_element_by_xpath("//input[@value='Delete']")
    button_delete.click()
    driver.find_element_by_xpath("//button/span").click()
