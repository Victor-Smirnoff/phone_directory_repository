class PageError(Exception):
    """
    Класс для описания ошибки номера страницы справочника
    """
    def __init__(self, page_number, max_lines_per_page, message='Ошибка на странице'):
        """
        Инициализатор класса, принимает номер страницы и инициализирует сообщение об ошибке
        :param page_number: номер страницы
        :param max_lines_per_page: максимальное количество записей на одной странице
        :param message: сообщение об ошибке
        """
        self.page_number = page_number
        self.max_lines_per_page = max_lines_per_page
        self.message = f'{message}: {page_number}'
        super().__init__(self.message)

    def __str__(self):
        return f'Ошибка со входными данными. Некорректный номер страницы “{self.page_number}” или некорректно указано количество записей на одной странице “{self.max_lines_per_page}”'


class LineError(Exception):
    def __init__(self, line_id, message='Ошибка поиска записи с id'):
        self.line_id = line_id
        self.message = f'{message}: “{self.line_id}”. Запись не найдена'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'