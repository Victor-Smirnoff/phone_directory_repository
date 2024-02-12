from DAO_phone_directory_repository import PhoneDirectoryRepository


class Handler:
    """
    Класс для выполнения всех реализованных возможностей по работе с телефонным справочником
    """
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

            dao_obj = PhoneDirectoryRepository()
            lines = dao_obj.get_line_dict(page, max_lines_per_page)

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