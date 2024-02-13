from DAO_phone_directory_repository import PhoneDirectoryRepository
from model import PhoneDirectoryModel


class Handler:
    """
    Класс для выполнения всех реализованных возможностей по работе с телефонным справочником
    """

    dao_obj = PhoneDirectoryRepository()

    def get_line_dict_handler(self):
        """
        Метод работает в цикле после ввода пользователя цифры 1.
        Обрабатывает запросы на вывод постранично записей из справочника на экран
        :return: None
        """
        while True:
            print()
            print('Вывод постранично записей из справочника на экран')

            page = input('Введите номер страницы: ')
            while True:
                if not self.validate_param(page):
                    page = input('Введите КОРРЕКТНО номер страницы: ')
                else:
                    break

            max_lines_per_page = input('Введите максимальное количество записей на одной странице: ')
            while True:
                if not self.validate_param(max_lines_per_page):
                    max_lines_per_page = input('Введите КОРРЕКТНО максимальное количество записей на одной странице: ')
                else:
                    break

            page = int(page)
            max_lines_per_page = int(max_lines_per_page)

            lines = self.dao_obj.get_line_dict(page, max_lines_per_page)

            if type(lines) is dict:
                print()
                print(*lines.values(), sep='\n')
            else:
                print()
                print(lines)

            print()
            print('Повторить вывод постранично записей из справочника на экран, напишите цифру 1')
            print('Выйти в главное меню - напишите что угодно кроме цифры 1 или ничего не пишите')

            answer = input('Напишите 1 или что-то другое: ')

            if answer != '1':
                print()
                print('Выход в главное меню')
                print()
                break
            else:
                continue

    @staticmethod
    def validate_param(param):
        """
        Метод для валидации введенных чисел пользователем
        :param param: целое число
        :return: тип bool возвращает True если введенное значение можно преобразовать в int, иначе - False
        """
        try:
            int(param)
            return True
        except ValueError:
            return False

    def add_line_handler(self):
        """
        Метод работает в цикле после ввода пользователя цифры 2.
        Обрабатывает запросы на добавление новой записи в справочник
        :return: None
        """
        while True:
            print('Добавление новой записи в справочник')
            print()
            print('Для добавления новой записи в справочник необходимо ввести следующие данные')
            print()
            surname = input('Введите фамилию: ')
            name = input('Введите имя: ')
            patronymic = input('Введите отчество: ')
            organization_name = input('Введите название организации: ')
            work_phone = input('Введите телефон рабочий: ')
            personal_phone = input('Введите телефон личный (сотовый): ')
            new_line_id = self.dao_obj.get_last_id() + 1

            new_line_obj = PhoneDirectoryModel(new_line_id,
                                               surname,
                                               name,
                                               patronymic,
                                               organization_name,
                                               work_phone,
                                               personal_phone)

            try:
                self.dao_obj.add_line(new_line_obj)

                result_dict = {'id': new_line_id,
                               'фамилия': surname,
                               'имя': name,
                               'отчество': patronymic,
                               'название организации': organization_name,
                               'телефон рабочий': work_phone,
                               'телефон личный (сотовый)': personal_phone
                               }

                print()
                print('Добавление новой записи в справочник выполнено успешно!')
                print()
                print(str(result_dict))

            except Exception as e:
                print()
                print(f'Ошибка добавления новой записи {str(e)}')

            print()
            print('Для добавления новой записи в справочник - нажмите 2')
            print('Выйти в главное меню - напишите что угодно кроме цифры 2')

            answer = input('Напишите 2 или что-то другое: ')
            if answer != '2':
                print()
                break
            else:
                continue

    def edit_line_handler(self):
        """
        Метод работает в цикле после ввода пользователя цифры 3.
        Обрабатывает запросы на редактирование записи в справочнике
        :return: None
        """

    def find_line_handler(self):
        """
        Метод работает в цикле после ввода пользователя цифры 4.
        Обрабатывает запросы на поиск записей по одной или нескольким характеристикам
        :return: None
        """
        while True:
            print()
            print('Поиск записей по одной или нескольким характеристикам')
            print()
            print('Для поиска по одной характеристике напишите 1')
            print('Для поиска по нескольким характеристикам напишите 2')
            print('Для выхода напишите что угодно, кроме 1 и 2')
            print()
            find_method = input('Введите 1 или 2: ')

            if find_method not in ('1', '2'):
                print()
                print('Выход из меню поиска записей')
                print()
                break

            if find_method == '1':
                result_of_work_func = self.find_line_one_param_handler()
                if result_of_work_func is None:
                    continue
                else:
                    break

            if find_method == '2':
                result_of_work_func = self.find_line_several_param_handler()
                if result_of_work_func is None:
                    continue
                else:
                    break

    def find_line_one_param_handler(self):
        """
        Метод обрабатывает поиск записей по одному параметру
        :return: None если введены числа 1,2,3,4,5,6,7, а иначе False
        """
        print()
        print('Поиск записей возможен по следующим характеристикам:')
        print('1 - по айди записи')
        print('2 - по фамилии')
        print('3 - по имени')
        print('4 - по отчеству')
        print('5 - по названию организации')
        print('6 - по телефону рабочему')
        print('7 - по телефону личный (сотовый)')
        print()
        print('Для выхода введите любой символ, отличный от цифр 1-7')
        print()
        find_param = input('Для поиска введите одну из следующих цифр 1,2,3,4,5,6,7: ')

        if find_param not in ('1', '2', '3', '4', '5', '6', '7'):
            return False

        routes = {
            '1': self.find_by_id_handler,
            '2': self.find_by_surname_handler,
            '3': self.find_by_name_handler,
            '4': self.find_by_patronymic_handler,
            '5': self.find_by_organization_name_handler,
            '6': self.find_by_work_phone_handler,
            '7': self.find_by_personal_phone_handler,
        }

        handler = routes[find_param]
        handler()

    def find_line_several_param_handler(self):
        """
        Метод обрабатывает поиск записей по нескольким параметрам
        :return: None если введены числа 1 2 3 4 5 6 7, а иначе False
        """
        print()
        print('Поиск записей возможен по следующим характеристикам:')
        print('1 - по айди записи')
        print('2 - по фамилии')
        print('3 - по имени')
        print('4 - по отчеству')
        print('5 - по названию организации')
        print('6 - по телефону рабочему')
        print('7 - по телефону личный (сотовый)')
        print()
        print('Для поиск записей по нескольким характеристикам введите числа от 1 до 7 через пробел:')
        print()
        print('Для выхода введите любой нечисловой символ')
        print()
        find_param = input('Для поиска введите через пробел следующие из цифр 1,2,3,4,5,6,7: ')

        find_param = find_param.split()
        for param in find_param:
            if param not in ('1', '2', '3', '4', '5', '6', '7'):
                return False

        routes = {
            '1': {'message': 'Введите айди записи', 'dao_func': self.dao_obj.find_by_id,
                  'param_name': 'line_id', 'rus_name': 'id'},
            '2': {'message': 'Введите фамилию', 'dao_func': self.dao_obj.find_by_surname,
                  'param_name': 'surname', 'rus_name': 'фамилия'},
            '3': {'message': 'Введите имя', 'dao_func': self.dao_obj.find_by_name,
                  'param_name': 'name', 'rus_name': 'имя'},
            '4': {'message': 'Введите отчество', 'dao_func': self.dao_obj.find_by_patronymic,
                  'param_name': 'patronymic', 'rus_name': 'отчество'},
            '5': {'message': 'Введите название организации', 'dao_func': self.dao_obj.find_by_organization_name,
                  'param_name': 'organization_name', 'rus_name': 'название организации'},
            '6': {'message': 'Введите телефон рабочий', 'dao_func': self.dao_obj.find_by_work_phone,
                  'param_name': 'work_phone', 'rus_name': 'телефон рабочий'},
            '7': {'message': 'Введите телефон личный (сотовый)', 'dao_func': self.dao_obj.find_by_personal_phone,
                  'param_name': 'personal_phone', 'rus_name': 'телефон личный (сотовый)'},
        }

        for param in find_param:
            data = input(f'{routes[param]['message']}: ')
            routes[param]['input'] = data

        params_to_search = [value for value in routes.values() if 'input' in value]

        # словарь для записи результатов поиска
        # ключи - это названия переменных, по которым искали
        # значения - это найденный результат - список или объект класса ошибки
        search_result = {}
        for param in params_to_search:
            param_dao_func = param['dao_func']
            found_lines = param_dao_func(param['input'])
            search_result[param['param_name']] = found_lines

        # дальнейший анализ переменной search_result
        # если по каждому из ключей лежит список с объектами класса PhoneDirectoryModel
        # и если в каждом списке есть один и тот же объект класса PhoneDirectoryModel
        # то это и есть искомый результат
        # а если нету, то вернуть сообщение типа "запись с параметрами {param: value} не найдена"

        if self.check_several_result(search_result):
            found_lines = self.get_several_result(search_result)
            print()
            print('Запись в справочнике найдена!')
            print()
            print(f'Найдено записей: {len(found_lines)}')
            print()
            print(*found_lines, sep='\n')
            print()
        else:
            print()
            print(f'Запись в справочнике не найдена')
            print()

    def check_several_result(self, search_result):
        """
        Метод проверяет результаты поиска по нескольким характеристикам
        :param search_result: словарь с результатами поиска
        ключи - это параметры, по которым искали запись, а значения - это то что нашли
        :return: тип bool - True если результат поиска положительный, иначе - False
        """
        for result in search_result.values():
            if type(result) is not list:
                return False

        res_set_list = []
        for result in search_result.values():
            result = set(result)
            res_set_list.append(result)

        for i in range(1, len(res_set_list)):
            intersection_result = res_set_list[0] & res_set_list[i]
            if not intersection_result:
                return False

        return True

    def get_several_result(self, search_result):
        """
        Метод используется после проверки результатов поиска по нескольким характеристикам.
        Когда точно известно, что есть хотя бы одна найденная запись
        :param search_result: словарь с результатами поиска
        ключи - это параметры, по которым искали запись, а значения - это то что нашли
        :return: список с найденными записями - объектами класса PhoneDirectoryModel
        """
        res_set_list = []
        for result in search_result.values():
            result = set(result)
            res_set_list.append(result)

        found_lines = []
        for i in range(1, len(res_set_list)):
            intersection_result = res_set_list[0] & res_set_list[i]
            for obj in intersection_result:
                if obj not in found_lines:
                    found_lines.append(obj)

        return found_lines

    def find_by_id_handler(self):
        """
        Метод выполняет обработку поиска по айди
        :return: None
        """
        print()
        print('Для поиска по айди записи необходимо ввести целое число id')
        line_id = input('Введите айди записи: ')
        while True:
            if not self.validate_param(line_id):
                line_id = input('Введите КОРРЕКТНО айди записи: ')
            else:
                break

        line_id = int(line_id)
        found_lines = self.dao_obj.find_by_id(line_id)
        if type(found_lines) is list:
            print()
            print(f'Запись в справочнике с айди “{line_id}” найдена!')
            print()
            print(*found_lines, sep='\n')
            print()
        else:
            print()
            print(f'Запись в справочнике с айди “{line_id}” не найдена')
            print()
            print(found_lines)
            print()

    def find_by_surname_handler(self):
        """
        Метод выполняет обработку поиска по фамилии
        :return: None
        """
        print()
        print('Для поиска по фамилии необходимо ввести фамилию')
        surname = input('Введите фамилию: ')
        found_lines = self.dao_obj.find_by_surname(surname)
        if type(found_lines) is list:
            print()
            print(f'Запись в справочнике с фамилией “{surname}” найдена!')
            print(f'Количество записей найдено “{len(found_lines)}”')
            print()
            print(*found_lines, sep='\n')
            print()
        else:
            print()
            print(f'Запись в справочнике с фамилией “{surname}” не найдена')
            print(found_lines)
            print()

    def find_by_name_handler(self):
        """
        Метод выполняет обработку поиска по имени
        :return: None
        """
        print()
        print('Для поиска по имени необходимо ввести имя')
        name = input('Введите имя: ')
        found_lines = self.dao_obj.find_by_name(name)
        if type(found_lines) is list:
            print()
            print(f'Запись в справочнике с именем “{name}” найдена!')
            print(f'Количество записей найдено “{len(found_lines)}”')
            print()
            print(*found_lines, sep='\n')
            print()
        else:
            print()
            print(f'Запись в справочнике с именем “{name}” не найдена')
            print(found_lines)
            print()

    def find_by_patronymic_handler(self):
        """
        Метод выполняет обработку поиска по отчеству
        :return: None
        """
        print()
        print('Для поиска по отчеству необходимо ввести отчество')
        patronymic = input('Введите отчество: ')
        found_lines = self.dao_obj.find_by_patronymic(patronymic)
        if type(found_lines) is list:
            print()
            print(f'Запись в справочнике с отчеством “{patronymic}” найдена!')
            print(f'Количество записей найдено “{len(found_lines)}”')
            print()
            print(*found_lines, sep='\n')
            print()
        else:
            print()
            print(f'Запись в справочнике с отчеством “{patronymic}” не найдена')
            print(found_lines)
            print()

    def find_by_organization_name_handler(self):
        """
        Метод выполняет обработку поиска по названию организации
        :return: None
        """
        print()
        print('Для поиска по названию организации необходимо ввести название организации')
        organization_name = input('Введите название организации: ')
        found_lines = self.dao_obj.find_by_organization_name(organization_name)
        if type(found_lines) is list:
            print()
            print(f'Запись в справочнике с названием организации “{organization_name}” найдена!')
            print(f'Количество записей найдено “{len(found_lines)}”')
            print()
            print(*found_lines, sep='\n')
            print()
        else:
            print()
            print(f'Запись в справочнике с названием организации “{organization_name}” не найдена')
            print(found_lines)
            print()

    def find_by_work_phone_handler(self):
        """
        Метод выполняет обработку поиска по телефону рабочему
        :return: None
        """
        print()
        print('Для поиска по телефону рабочему необходимо ввести телефон рабочий')
        work_phone = input('Введите телефон рабочий: ')
        found_lines = self.dao_obj.find_by_work_phone(work_phone)
        if type(found_lines) is list:
            print()
            print(f'Запись в справочнике с телефоном рабочим “{work_phone}” найдена!')
            print(f'Количество записей найдено “{len(found_lines)}”')
            print()
            print(*found_lines, sep='\n')
            print()
        else:
            print()
            print(f'Запись в справочнике с телефоном рабочим “{work_phone}” не найдена')
            print(found_lines)
            print()

    def find_by_personal_phone_handler(self):
        """
        Метод выполняет обработку поиска по телефону личному (сотовому)
        :return: None
        """
        print()
        print('Для поиска по телефону личному (сотовому) необходимо ввести телефон личный')
        personal_phone = input('Введите телефон личный: ')
        found_lines = self.dao_obj.find_by_personal_phone(personal_phone)
        if type(found_lines) is list:
            print()
            print(f'Запись в справочнике с телефоном личным “{personal_phone}” найдена!')
            print(*found_lines, sep='\n')
            print()
        else:
            print()
            print(f'Запись в справочнике с телефоном личным “{personal_phone}” не найдена')
            print(found_lines)
            print()
