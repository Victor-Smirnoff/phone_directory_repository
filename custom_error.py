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
        return f'{self.message}'


class LineError(Exception):
    """
    Класс для описания ошибки поиска записи в справочнике
    """
    def __init__(self, message):
        """
        Инициализатор класса, содержит сообщение об ошибке
        :param message: сообщение об ошибке
        """
        self.message = message

    def __str__(self):
        return f'{self.message}'
