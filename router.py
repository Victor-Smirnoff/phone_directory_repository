from handler import Handler


class Router:
    """
    Класс роутер для выбора функции-обработчика
    """
    handler_obj = Handler()
    ROUTES = {
        '1': handler_obj.get_line_dict_handler,
        '2': handler_obj.add_line_handler,
        '3': handler_obj.edit_line_handler,
        '4': handler_obj.find_line_handler,
    }

    def determine_handler_method(self, key):
        """
        Метод возвращает тип функции-обработчика
        :param key: ключ словаря ROUTES
        :return: тип функции-обработчика из словаря ROUTES
        """
        return self.ROUTES.get(key)
