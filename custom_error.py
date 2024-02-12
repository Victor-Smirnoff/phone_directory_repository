class PageError(Exception):
    """
    Класс для описания ошибки номера страницы справочника
    """
    def __init__(self, page_number, message='Ошибка на странице'):
        """
        Инициализатор класса, принимает номер страницы и инициализирует сообщение об ошибке
        :param page_number: номер страницы
        :param message: сообщение об ошибке
        """
        self.page_number = page_number
        self.message = f'{message}: {page_number}'
        super().__init__(self.message)