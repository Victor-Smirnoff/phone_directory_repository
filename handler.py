from DAO_phone_directory_repository import PhoneDirectoryRepository
from model import PhoneDirectoryModel


class Handler:
    """
    Класс для выполнения всех реализованных возможностей по работе с телефонным справочником
    """

    dao_obj = PhoneDirectoryRepository()

    def get_line_dict_handler(self):
        """
        Метод работает в цикле после ввода пользователя цифры 1
        Обрабатывает запросы на вывод постранично записей из справочника на экран
        :return: None
        """
        while True:
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

            if type(lines) == dict:
                print(*lines.values(), sep='\n')
            else:
                print(lines)

            print()
            print('Повторить вывод постранично записей из справочника на экран, напишите цифру 1')
            print('Выйти в главное меню - напишите что угодно кроме цифры 1 или ничего не пишите')

            answer = input('Напишите 1 или что-то другое: ')

            if answer != '1':
                print()
                break
            else:
                continue

    def validate_param(self, param):
        """
        Метод для валидации введенных чисел пользователем
        :param param: целое число
        :return: тип bool возвращает True если введенное значение можно преобразовать в int, иначе - False
        """
        try:
            param = int(param)
            return True
        except Exception as e:
            return False

    def add_line_handler(self):
        """
        Метод работает в цикле после ввода пользователя цифры 2
        Обрабатывает запросы на добавление новой записи в справочник
        :return: None
        """
        while True:
            print('Добавление новой записи в справочник')
            print()
            print('Для добавления новой записи в справочник необходимо ввести следующие данные')
            print()
            sirname = input('Введите фамилию: ')
            name = input('Введите имя: ')
            patronym = input('Введите отчество: ')
            organization_name = input('Введите название организации: ')
            work_phone = input('Введите телефон рабочий: ')
            personal_phone = input('Введите телефон личный (сотовый): ')
            new_line_id = self.dao_obj.get_last_id() + 1

            new_line_obj = PhoneDirectoryModel(new_line_id, sirname, name, patronym, organization_name, work_phone, personal_phone)

            try:
                self.dao_obj.add_line(new_line_obj)

                result_dict = {}
                result_dict['id'] = new_line_id
                result_dict['фамилия'] = sirname
                result_dict['имя'] = name
                result_dict['отчество'] = patronym
                result_dict['название организации'] = organization_name
                result_dict['телефон рабочий'] = work_phone
                result_dict['телефон личный (сотовый)'] = personal_phone
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
        Метод работает в цикле после ввода пользователя цифры 3
        Обрабатывает запросы на редактирование записи в справочнике
        :return: None
        """

    def find_line_handler(self):
        """
        Метод работает в цикле после ввода пользователя цифры 4
        Обрабатывает запросы на поиск записей по одной или нескольким характеристикам
        :return: None
        """
        while True:
            print('Поиск записей по одной или нескольким характеристикам')
            print()
            print('Для поиска по одной характеристике напишите 1')
            print('Для поиска по нескольким характеристикам напишите 2')
            print('Для выхода напишите что угодно, кроме 1 и 2')
            print()
            find_method = input('Введите 1 или 2: ')

            if find_method not in ('1', '2'):
                break
                print()

            if find_method == '1':
                print('Поиск записей возможен по следующим характеристикам:')
                print('1 - по айди записи')
                print('2 - по фамилии')
                print('3 - по имени')
                print('4 - по отчеству')
                print('5 - по названию организации')
                print('6 - по телефону рабочему')
                print('7 - по телефону личный (сотовый)')
                print('Для выхода введите любой символ, отличный от цифр 1-7')
                print()
                find_param = input('Для поиска введите одну из следующих цифр 1,2,3,4,5,6,7: ')

                if find_param not in ('1', '2', '3', '4', '5', '6', '7'):
                    break

                if find_param == '1':
                    print()
                    print('Для поиска по айди записи необходимо ввести целое число id')
                    line_id = input('Введите айди записи: ')
                    while True:
                        if not self.validate_param(line_id):
                            line_id = input('Введите КОРРЕКТНО айди записи: ')
                        else:
                            break

                    line_id = int(line_id)
                    found_line = self.dao_obj.find_by_id(line_id)
                    if type(found_line) == dict:
                        print()
                        print('Запись в справочнике найдена!')
                    else:
                        print()
                        print('Запись в справочнике не найдена')
                    print(found_line)
                    print()
