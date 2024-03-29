import csv
from tempfile import NamedTemporaryFile
import shutil

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
                dict_reader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                if page == 1:
                    result = {}
                    for _ in range(max_lines_per_page):
                        row = next(dict_reader_obj, None)
                        if row is not None:
                            result[row['id']] = row
                else:
                    result = {}
                    for _ in range(page * max_lines_per_page - max_lines_per_page):
                        next(dict_reader_obj)
                    for _ in range(max_lines_per_page):
                        row = next(dict_reader_obj, None)
                        if row is not None:
                            result[row['id']] = row

            return result

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    @staticmethod
    def validate_page(page, max_lines_per_page):
        """
        Метод для валидации входных параметров номер страницы и количества записей на странице
        Если параметры валидные, то метод вернет None, иначе - возбуждает исключение
        :param page: номер страницы
        :param max_lines_per_page: количество записей на странице
        :return: None
        """
        if type(page) is not int:
            message = f'Ошибка со входными данными. Некорректный номер страницы “{page}”'
            raise PageError(message)
        if type(max_lines_per_page) is not int:
            message = (f'Ошибка со входными данными. '
                       f'Некорректно указано количество записей на одной странице “{max_lines_per_page}”')
            raise PageError(message)
        if type(max_lines_per_page) is int and max_lines_per_page <= 0:
            message = f'Ошибка со входными данными. Страницы с номером “{page}” не существует'
            raise PageError(message)

        with open(CSV_FILE, 'r', encoding='UTF-8') as csv_file:
            dict_reader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

            row_count = sum(1 for _ in dict_reader_obj)
            ml = max_lines_per_page
            pages = (row_count // ml) + 1 if not (row_count % ml) else (row_count // ml) + 2
            if page not in range(1, pages):
                message = (f'Ошибка со входными данными. Страницы с номером “{page}” не существует. '
                           f'Для “{max_lines_per_page}” в справочнике есть “{pages}” страниц')
                raise PageError(message)

    @staticmethod
    def add_line(new_line_obj: PhoneDirectoryModel):
        """
        Метод записывает новую строчку в файл
        :param new_line_obj: объект класса PhoneDirectoryModel
        :return: None
        """
        new_line_id = new_line_obj.line_id
        surname = new_line_obj.surname
        name = new_line_obj.name
        patronymic = new_line_obj.patronymic
        organization_name = new_line_obj.organization_name
        work_phone = new_line_obj.work_phone
        personal_phone = new_line_obj.personal_phone

        with (open(CSV_FILE, 'a+', encoding='UTF-8', newline='') as csv_file):
            writer = csv.writer(csv_file, delimiter=';')
            writer.writerow((new_line_id, surname, name, patronymic, organization_name, work_phone, personal_phone))

    @staticmethod
    def get_last_id():
        """
        Метод возвращает последний записанный id в csv файле CSV_FILE
        :return: число номер id или значение ValueError
        """
        with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
            dict_reader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

            last_line = None

            for row in dict_reader_obj:
                if row:
                    last_line = row

            try:
                last_id = int(last_line['id'])
                return last_id
            except ValueError('Ошибка: значение id записи не является целым числом') as e:
                return e

    @staticmethod
    def get_phone_directory_model_obj(row):
        """
        Метод создает объект класса PhoneDirectoryModel и возвращает его
        :param row: словарь с данными по строке
        :return: объект PhoneDirectoryModel
        """
        line_id = row['id']
        surname = row['фамилия']
        name = row['имя']
        patronymic = row['отчество']
        organization_name = row['название организации']
        work_phone = row['телефон рабочий']
        personal_phone = row['телефон личный (сотовый)']
        obj = PhoneDirectoryModel(line_id, surname, name, patronymic, organization_name, work_phone, personal_phone)
        return obj

    def find_by_id(self, line_id):
        """
        Метод для поиска записи в справочнике по айди записи
        :param line_id: айди записи
        :return: список найденных записей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_reader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_lines = []

                for row in dict_reader_obj:
                    if row and int(row['id']) == line_id:
                        obj = self.get_phone_directory_model_obj(row)
                        found_lines.append(obj)

                if found_lines:
                    return found_lines
                else:
                    message = f'Запись с айди “{line_id}” не найдена'
                    raise LineError(message)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def find_by_surname(self, surname):
        """
        Метод для поиска записи в справочнике по фамилии
        :param surname: фамилия
        :return: список найденных записей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_reader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_lines = []

                for row in dict_reader_obj:
                    if row and row['фамилия'] == surname:
                        obj = self.get_phone_directory_model_obj(row)
                        found_lines.append(obj)

                if found_lines:
                    return found_lines
                else:
                    message = f'Запись с фамилией “{surname}” не найдена'
                    raise LineError(message)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def find_by_name(self, name):
        """
        Метод для поиска записи в справочнике по имени
        :param name: имя
        :return: список найденных записей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_reader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_lines = []

                for row in dict_reader_obj:
                    if row and row['имя'] == name:
                        obj = self.get_phone_directory_model_obj(row)
                        found_lines.append(obj)

                if found_lines:
                    return found_lines
                else:
                    message = f'Запись с именем “{name}” не найдена'
                    raise LineError(message)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def find_by_patronymic(self, patronymic):
        """
        Метод для поиска записи в справочнике по отчеству
        :param patronymic: отчество
        :return: список найденных записей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_reader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_lines = []

                for row in dict_reader_obj:
                    if row and row['отчество'] == patronymic:
                        obj = self.get_phone_directory_model_obj(row)
                        found_lines.append(obj)

                if found_lines:
                    return found_lines
                else:
                    message = f'Запись с отчеством “{patronymic}” не найдена'
                    raise LineError(message)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def find_by_organization_name(self, organization_name):
        """
        Метод для поиска записи в справочнике по названию организации
        :param organization_name: название организации
        :return: список найденных записей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_reader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_lines = []

                for row in dict_reader_obj:
                    if row and row['название организации'] == organization_name:
                        obj = self.get_phone_directory_model_obj(row)
                        found_lines.append(obj)

                if found_lines:
                    return found_lines
                else:
                    message = f'Запись с организацией “{organization_name}” не найдена'
                    raise LineError(message)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def find_by_work_phone(self, work_phone):
        """
        Метод для поиска записи в справочнике по телефону рабочий
        :param work_phone: телефон рабочий
        :return: список найденных записей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_reader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_lines = []

                for row in dict_reader_obj:
                    if row and row['телефон рабочий'] == work_phone:
                        obj = self.get_phone_directory_model_obj(row)
                        found_lines.append(obj)

                if found_lines:
                    return found_lines
                else:
                    message = f'Запись с рабочим телефоном “{work_phone}” не найдена'
                    raise LineError(message)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    def find_by_personal_phone(self, personal_phone):
        """
        Метод для поиска записи в справочнике по телефону личный (сотовый)
        :param personal_phone: телефон личный (сотовый)
        :return: список найденных записей с данными по строке или объект класса LineError если ничего не найдено
        """
        try:
            with open(CSV_FILE, 'r', encoding='UTF-8', newline='') as csv_file:
                dict_reader_obj = csv.DictReader(csv_file, delimiter=';', quotechar='"')

                found_lines = []

                for row in dict_reader_obj:
                    if row and row['телефон личный (сотовый)'] == personal_phone:
                        obj = self.get_phone_directory_model_obj(row)
                        found_lines.append(obj)

                if found_lines:
                    return found_lines
                else:
                    message = f'Запись с личным телефоном “{personal_phone}” не найдена'
                    raise LineError(message)

        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response

    @staticmethod
    def edit_line(phone_directory_model: PhoneDirectoryModel):
        """
        Метод для редактирования записей в справочнике.
        Если всё успешно, то метод открывает файл в режиме чтения, создает временный файл tmp.
        По одной строке читает исходный файл.
        Если строка требует редактирования, то записывает новую строку во временный файл.
        Если строка не требуется редактирования, то записывает строку в исходном виде во временный файл.
        Когда запись завершена, происходит запись содержимого временного файла в основной файл.
        :param phone_directory_model: Готовый объект класса PhoneDirectoryModel с отредактированными данными
        :return: None или объект ошибки класса ErrorResponse если не получилось перезаписать данные
        """
        try:
            temp_file = NamedTemporaryFile(mode='w', encoding='UTF-8', delete=False)

            with open(CSV_FILE, 'r', encoding='UTF-8') as csvfile, temp_file:
                reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
                first_string = ';'.join(reader.fieldnames)
                print(first_string, file=temp_file)
                for row in reader:
                    if str(row['id']) == str(phone_directory_model.line_id):
                        print(f'Редактирование строки с айди: “{row['id']}”')
                        new_row = {
                            'id': str(phone_directory_model.line_id),
                            'фамилия': phone_directory_model.surname,
                            'имя': phone_directory_model.name,
                            'отчество': phone_directory_model.patronymic,
                            'название организации': phone_directory_model.organization_name,
                            'телефон рабочий': phone_directory_model.work_phone,
                            'телефон личный (сотовый)': phone_directory_model.personal_phone,
                        }
                        string_to_write = ';'.join(new_row.values())
                        print(string_to_write, file=temp_file)
                    else:
                        if row:
                            string_to_write = ';'.join(row.values())
                            print(string_to_write, file=temp_file)
                        else:
                            print('', file=temp_file)

            shutil.move(temp_file.name, CSV_FILE)
            print()
            print(f'Редактирование строки с айди: “{new_row['id']}” прошло успешно!')
            print()
            print(phone_directory_model)
            print()
        except Exception as e:
            error_type = {str(e)}
            message = 'Произошла ошибка записи данных в справочник, попробуйте позже'
            error_response = ErrorResponse(error_type=error_type, message=message)
            return error_response
