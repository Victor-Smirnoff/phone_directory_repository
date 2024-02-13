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

    def __repr__(self):
        return (f'{{“id”: “{self.line_id}”, “фамилия”: “{self.surname}”, “имя: “{self.name}”, '
                f'“отчество”: “{self.patronymic}”, “название организации”: “{self.organization_name}”, '
                f'“телефон рабочий”: “{self.work_phone}”, “телефон личный (сотовый)”: “{self.personal_phone}”}}')

    def __hash__(self):
        obj_string = str(self.line_id) + self.surname + self.name + self.patronymic + self.organization_name + self.work_phone + self.personal_phone
        return hash(obj_string)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.line_id != other.line_id:
            return False
        if self.surname != other.surname:
            return False
        if self.name != other.name:
            return False
        if self.patronymic != other.patronymic:
            return False
        if self.organization_name != other.organization_name:
            return False
        if self.work_phone != other.work_phone:
            return False
        if self.personal_phone != other.personal_phone:
            return False

        return True