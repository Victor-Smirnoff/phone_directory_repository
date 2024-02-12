import csv



class PhoneDirectoryRepository:
    """
    Класс для доступа к данным телефонного справочника из файла phone_directory_data.csv
    """

    def get_line_list(self, page: int = 1, max_lines_per_page: int = 5):
        """
        Метод выполняет вывод постранично записей из справочника на экран
        :param page: номер страницы
        :param max_lines_per_page: максимальное количество записей на одной странице
        :return: итерируемый объект со строками для печати их в консоль
        """
        try:
            with open('phone_directory_data.csv', 'r', encoding='UTF-8') as file:
                dict_redader_obj = csv.DictReader(file, delimiter=';', quotechar='"')


            return dict_redader_obj

        except Exception as e:
            message = {'message': f'Произошла ошибка чтения справочника - {str(e)}'}
            return message


phone_directory_obj = PhoneDirectoryRepository()
dict_redader_obj = phone_directory_obj.get_line_list()
for row in dict_redader_obj:
    print(row)