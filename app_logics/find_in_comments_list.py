__author__ = 'nshumakov'


class FindInCommentsList(object):
    """
    Class to find the required elements on all pages of the site
    """

    def __init__(self, web_driver):
        self.__driver = web_driver

    def search_in_list_by_comment(self) -> list:

        """
        Function-finder the required elements on all pages by entered comment
        :return:

        """

        list_el = self.__driver.find_element_by_class_name(
            "webgrid-footer")
        list_a = list_el.find_elements_by_tag_name("a")
        href = set()
        text_columns = list()
        for link_a in list_a:
            href.add(link_a.get_attribute("href"))

        for ref in href:
            self.__driver.get(ref)
            list_columns = self.__driver.find_elements_by_class_name(
                "textcolumn")
            for column in list_columns:
                text_columns.append(column.text)

        return text_columns

    def search_in_list_by_number(self) -> list:

        """
        Function-finder the required elements on all pages by entered number
        :return:

        """

        list_el = self.__driver.find_element_by_class_name("webgrid-footer")
        list_a = list_el.find_elements_by_tag_name("a")
        href = set()
        number_columns = list()
        for link_a in list_a:
            href.add(link_a.get_attribute("href"))

        for ref in href:
            self.__driver.get(ref)
            list_columns = self.__driver.find_elements_by_class_name(
                "numbercolumn")
            for column in list_columns:
                number_columns.append(int(column.text))

        return number_columns
