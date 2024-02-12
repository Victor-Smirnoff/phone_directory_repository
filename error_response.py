"""
Здесь описан класс для хранения данных по ответу с какой-либо ошибкой
"""


class ErrorResponse:
    """
    Класс для хранения данных по ответу с какой-либо ошибкой
    """
    def __init__(self, error_type, message):
        """
        :param error_type: тип ошибки
        :param message: сообщение ответа
        """
        self.error_type = error_type
        self.message = message

    def __str__(self):
        return str({"message": self.message, "error_type": self.error_type})