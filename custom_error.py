class PageError(Exception):
    """
    Класс для описания ошибки номера страницы справочника
    """
    def __init__(self, message):
        """
        Инициализатор класса, содержит сообщение об ошибке
        :param message: сообщение об ошибке
        """
        self.message = message

    def __str__(self):
        return f'Ошибка со входными данными. Некорректный номер страницы “{self.page_number}” или некорректно указано количество записей на одной странице “{self.max_lines_per_page}”'


class LineError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}'