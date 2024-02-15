import unittest
import io
import sys


from DAO_phone_directory_repository import PhoneDirectoryRepository
from custom_error import PageError, LineError
from error_response import ErrorResponse


dao_obj = PhoneDirectoryRepository()


class TestGetLineDict(unittest.TestCase):
    def test_return_type(self):
        result = dao_obj.get_line_dict(page=1, max_lines_per_page=3)
        self.assertIsInstance(result, (dict, ErrorResponse, PageError),
                              'Функция должна возвращать словарь или объект ErrorResponse')

        result = dao_obj.get_line_dict(page=1000, max_lines_per_page=1000)
        self.assertIsInstance(result, (dict, ErrorResponse, PageError), 'Функция должна возвращать PageError')

        result = dao_obj.get_line_dict(page='abc', max_lines_per_page='abc')
        self.assertIsInstance(result, (dict, ErrorResponse, PageError), 'Функция должна возвращать PageError')

    def test_max_lines_per_page(self):
        max_lines_per_page = 3
        result = dao_obj.get_line_dict(page=1, max_lines_per_page=max_lines_per_page)
        self.assertEqual(len(result), max_lines_per_page, f'Длина возвращаемого словаря не соответствует ожидаемой')


class TestGetLastID(unittest.TestCase):
    def test_last_id_type(self):
        result = dao_obj.get_last_id()
        self.assertIsInstance(result, (int, ValueError),
                              'Функция должна возвращать целое число или объект ValueError')


class TestFindByID(unittest.TestCase):
    def test_find_by_id_type(self):
        result = dao_obj.find_by_id(1)
        self.assertIsInstance(result, (list, ErrorResponse),
                              'Функция должна возвращать список или объект ErrorResponse')

        result = dao_obj.find_by_id(1000)
        self.assertIsInstance(result, (list, ErrorResponse),
                              'Функция должна возвращать список или объект ErrorResponse')


if __name__ == "__main__":
    unittest.main()
