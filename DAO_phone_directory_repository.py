import csv

from custom_error import PageError
from error_response import ErrorResponse


class PhoneDirectoryRepository:
    """
    Класс для доступа к данным телефонного справочника из файла phone_directory_data.csv
    """

    def get_line_dict(self, page: int = 1, max_lines_per_page: int = 5):
        """
        Метод выполняет вывод постранично записей из справочника на экран
        :param page: номер страницы
        :param max_lines_per_page: максимальное количество записей на одной странице
        :return: итерируемый объект со строками для печати их в консоль или объект класса ErrorResponse
        """
        try:
            with open('phone_directory_data.csv', 'r', encoding='UTF-8') as csv_file:
                dict_redader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                row_count = sum(1 for _ in dict_redader_obj)
                if page not in range(1, row_count + 1):
                    raise PageError(page)
                elif page == 1:
                    result = {}
                    for _ in range(max_lines_per_page):
                        row = next(dict_redader_obj, None)
                        if row is not None:
                            result[row['id']] = row
                else:
                    result = {}
                    for _ in range(page * max_lines_per_page - max_lines_per_page):
                        next(dict_redader_obj)
                    for _ in range(max_lines_per_page):
                        row = next(dict_redader_obj, None)
                        if row is not None:
                            result[row['id']] = row

            return result

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response


phone_directory_obj = PhoneDirectoryRepository()
row_count = phone_directory_obj.get_line_dict(page=0, max_lines_per_page=5)

print(row_count)