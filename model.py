class PhoneDirectoryModel:
    """
    Класс для описания модели записи в телефонном справочнике
    """
    def __init__(self, line_id, surname, name, patronymic, organization_name, work_phone, personal_phone):
        """
        Инициализатор класса
        :param line_id: айди записи
        :param surname: фамилия
        :param name: имя
        :param patronymic: отчество
        :param organization_name: название организации
        :param work_phone: телефон рабочий
        :param personal_phone: телефон личный (сотовый)
        """
        self.line_id = line_id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.organization_name = organization_name
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def __str__(self):
        return (f'{{“id”: “{self.line_id}”, “фамилия”: “{self.surname}”, “имя: “{self.name}”, '
                f'“отчество”: “{self.patronymic}”, “название организации”: “{self.organization_name}”, '
                f'“телефон рабочий”: “{self.work_phone}”, “телефон личный (сотовый)”: “{self.personal_phone}”}}')
