class PhoneDirectoryModel:
    """
    Класс для описания модели записи в телефонном справочнике
    """
    def __init__(self, line_id, sirname, name, patronym, organization_name, work_phone, personal_phone):
        """
        Инициализатор класса
        :param line_id: айди записи
        :param sirname: фамилия
        :param name: имя
        :param patronym: отчество
        :param organization_name: название организации
        :param work_phone: телефон рабочий
        :param personal_phone: телефон личный (сотовый)
        """
        self.line_id = line_id
        self.sirname = sirname
        self.name = name
        self.patronym = patronym
        self.organization_name = organization_name
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def __str__(self):
        return f'{self.__class__.__name__}({self.line_id}, {self.sirname}, {self.name}, {self.patronym}, {self.organization_name}, {self.work_phone}, {self.personal_phone})'