import csv

from custom_error import PageError, LineError
from error_response import ErrorResponse
from model import PhoneDirectoryModel

CSV_FILE = 'phone_directory_data.csv'


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
            self.validate_page(page, max_lines_per_page)
            with open(CSV_FILE, 'r', encoding='UTF-8') as csv_file:
                dict_redader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                if page == 1:
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

    def validate_page(self, page, max_lines_per_page):
        """
        Метод для валидации входных параметров номер страницы и количества записей на странице
        Если параметры валидные, то метод вернет None, иначе - возбуждает исключение
        :param page: номер страницы
        :param max_lines_per_page: количество записей на странице
        :return: None
        """
        if type(page) != int:
            raise PageError(page, max_lines_per_page)
        if type(max_lines_per_page) != int:
            raise PageError(page, max_lines_per_page)
        if type(max_lines_per_page) == int and max_lines_per_page <= 0:
            raise PageError(page, max_lines_per_page)

        with open(CSV_FILE, 'r', encoding='UTF-8') as csv_file:
            dict_redader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

            row_count = sum(1 for _ in dict_redader_obj)
            if page not in range(1, (row_count // max_lines_per_page) + 1):
                raise PageError(page, max_lines_per_page)

    def add_line(self, sirname: str, name: str, patronym: str, organization_name: str, work_phone: str, personal_phone: str):
        """
        Метод записывает новую строчку в файл
        :param sirname: фамилия
        :param name: имя
        :param patronym: отчество
        :param organization_name: название организации
        :param work_phone: телефон рабочий
        :param personal_phone: телефон личный (сотовый)
        :return: None
        """
        with open(CSV_FILE, 'a+', encoding='UTF-8', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            new_line_id = self.get_last_id() + 1
            writer.writerow((new_line_id, sirname, name, patronym, organization_name, work_phone, personal_phone))

    def get_last_id(self):
        """
        Метод возвращает последний записанный id в csv файле CSV_FILE
        :return: число номер id
        """
        with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
            dict_redader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

            last_line = None

            for row in dict_redader_obj:
                if row:
                    last_line = row

            return int(last_line['id'])

    def find_by_id(self, line_id):
        """
        Метод для поиска записи в справочнике по айди записи
        :param line_id: айди записи
        :return: словарь с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_redader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_line = None

                for row in dict_redader_obj:
                    if row and int(row['id']) == line_id:
                        found_line = row

                if found_line is not None:
                    return found_line
                else:
                    raise LineError(line_id)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def find_by_sirname(self, sirname):
        """
        Метод для поиска записи в справочнике по фамилии
        :param sirname: фамилия
        :return: список найденных словарей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_redader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_line = []

                for row in dict_redader_obj:
                    if row and row['фамилия'] == sirname:
                        found_line.append(row)

                if found_line:
                    return found_line
                else:
                    raise LineError(sirname)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def find_by_name(self, name):
        """
        Метод для поиска записи в справочнике по имени
        :param name: имя
        :return: список найденных словарей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_redader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_line = []

                for row in dict_redader_obj:
                    if row and row['имя'] == name:
                        found_line.append(row)

                if found_line:
                    return found_line
                else:
                    raise LineError(name)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def find_by_patronym(self, patronym):
        """
        Метод для поиска записи в справочнике по отчеству
        :param patronym: отчество
        :return: список найденных словарей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_redader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_line = []

                for row in dict_redader_obj:
                    if row and row['отчество'] == patronym:
                        found_line.append(row)

                if found_line:
                    return found_line
                else:
                    raise LineError(patronym)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def find_by_organization_name(self, organization_name):
        """
        Метод для поиска записи в справочнике по названию организации
        :param organization_name: название организации
        :return: список найденных словарей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_redader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_line = []

                for row in dict_redader_obj:
                    if row and row['название организации'] == organization_name:
                        found_line.append(row)

                if found_line:
                    return found_line
                else:
                    raise LineError(organization_name)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def find_by_work_phone(self, work_phone):
        """
        Метод для поиска записи в справочнике по телефону рабочий
        :param work_phone: телефон рабочий
        :return: список найденных словарей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_redader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_line = []

                for row in dict_redader_obj:
                    if row and row['телефон рабочий'] == work_phone:
                        found_line.append(row)

                if found_line:
                    return found_line
                else:
                    raise LineError(work_phone)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def find_by_personal_phone(self, personal_phone):
        """
        Метод для поиска записи в справочнике по телефону личный (сотовый)
        :param personal_phone: телефон личный (сотовый)
        :return: список найденных словарей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_redader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_line = []

                for row in dict_redader_obj:
                    if row and row['телефон личный (сотовый)'] == personal_phone:
                        found_line.append(row)

                if found_line:
                    return found_line
                else:
                    raise LineError(personal_phone)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def edit_line(self):
        """
        Метод для редактирования записей в справочнике
        :return:
        """





# phone_directory_obj = PhoneDirectoryRepository()
#
#
# new_line = 'Андреев;Олег;Игоревич;ООО СпортЛайн;+7 (495) 234-56-78;+7 (923) 456-78-90'.split(';')
#
# phone_directory_obj.add_line(*new_line)
#
#
# lines = phone_directory_obj.get_line_dict(page=3, max_lines_per_page=8)
#
# if type(lines) == dict:
#     print(*lines.values(), sep='\n')
# else:
#     print(lines)