"""
The package in which the preparation methods for testing the buttons are
   collected
"""

from selenium.webdriver.common.keys import Keys

__author__ = 'nshumakov'

SAVE_BUTTON_INDEX = 1
SAVE_N_RETURN_BUTTON_INDEX = 2
INDEX_TO_SWITCH_BETWEEN_PAGES = 5


def create_new_comment_save(driver, text_comment,
                            number_comment) -> None:
    """
    Click the "Save" button when typing less than 50 characters in the
       "Comment Text" field, also adding a number to the "Number"

    :param driver: web driver
    :param text_comment: comment prepared below
    :param number_comment: number for comment prepared below
    :return:

    """

    button_new = driver.find_element_by_id("newbutton")
    button_new.click()
    comment_field = driver.find_element_by_id("Text")
    comment_field.send_keys(text_comment)
    number_field = driver.find_element_by_id("Number")
    number_field.send_keys(number_comment)
    button_all_categories = driver.find_element_by_name("AllSelect")
    button_all_categories.click()
    button_save = driver.find_element_by_xpath(
        '//*[@id="editor-navigation"]/input[%d]' % SAVE_BUTTON_INDEX)
    button_save.click()
    button_return = driver.find_element_by_xpath(
        '//*[@id="logindisplay"]/a')
    button_return.click()


def create_new_comment_save_return(driver, text_comment) -> None:
    """

    Click the "Save & Return" button when typing less than 50 characters
        in the "Comment Text" field, also leaving the "Number" field empty

    :param driver: web driver
    :param text_comment: comment prepared below
    :return:

    """

    button_new = driver.find_element_by_id("newbutton")
    button_new.click()
    comment_field = driver.find_element_by_id("Text")
    comment_field.send_keys(text_comment)
    button_all_categories = driver.find_element_by_name("AllSelect")
    button_all_categories.click()
    button_save_and_return = driver.find_element_by_xpath(
        '//*[@id="editor-navigation"]/input[%d]'
        % SAVE_N_RETURN_BUTTON_INDEX)
    button_save_and_return.click()


def prepare_duplicate_button_for_test(driver, text_comment) -> None:
    """

    After clicking the "Duplicate" button, selecting one comment,
    clicking the "Save & Return" button when typing in the "Comment Text"

    :param driver: web driver
    :param text_comment: comment prepared below
    :return:

    """

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
    button_save_and_return = driver.find_element_by_xpath(
        "//input[@value='Save & Return']")
    button_save_and_return.click()


def prepare_edit_button_for_test(driver, text_comment) -> None:
    """

    After clicking the "Edit" button, selecting one comment, clicking
    the "Save & Return" button when typing the changes in the "Comment Text"

    :param driver: web driver
    :param text_comment: comment prepared below
    :return:

    """

    select_comment_for_edit = driver.find_element_by_name(
        "SelectedId")
    select_comment_for_edit.click()
    button_edit = driver.find_element_by_xpath(
        '//*[@id="command-navigation"]/input[%d]'
        % SAVE_N_RETURN_BUTTON_INDEX)
    button_edit.click()
    text_field = driver.find_element_by_id("Text")
    text_field.clear()
    text_field.send_keys(text_comment)
    button_save_and_return = driver.find_element_by_xpath(
        "//input[@value='Save & Return']")
    button_save_and_return.click()
    refresh_comments_list = driver.find_element_by_xpath(
        "//*[@id='main']/div/div[%d]/form/table/thead/tr/th[%d]/a"
        % (INDEX_TO_SWITCH_BETWEEN_PAGES, SAVE_N_RETURN_BUTTON_INDEX))
    refresh_comments_list.click()


def prepare_delete_button_for_tests(driver) -> None:
    """

    After clicking the "Delete" button, selecting one comment and pressing
       the confirmation in the dialog box

    :param driver: web driver
    :return:
    """

    refresh_comments_list = driver.find_element_by_xpath(
        "//*[@id='main']/div/div[%d]/form/table/thead/tr/th[%d]/a" %
        (INDEX_TO_SWITCH_BETWEEN_PAGES, SAVE_N_RETURN_BUTTON_INDEX))
    refresh_comments_list.click()
    select_comment_for_deleting = driver.find_element_by_name(
        "SelectedId")
    select_comment_for_deleting.click()
    button_delete = driver.find_element_by_xpath("//input[@value='Delete']")
    button_delete.click()
    driver.find_element_by_xpath("//button/span").click()
