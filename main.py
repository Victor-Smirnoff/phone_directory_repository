






def add_line(sirname: str, name: str, patronym: str, organization_name: str, work_phone: str, personal_phone: str):
    """
    Метод записывает новую строчку в файл
    :param sirname: фамилия
    :param name: имя
    :param patronym: отчество
    :param organization_name: название организации
    :param work_phone: телефон рабочий
    :param personal_phone: телефон личный (сотовый)
    :return: None
    """
    with open('phone_directory_data.csv', 'a+', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow((sirname, name, patronym, organization_name, work_phone, personal_phone))


def edit_line():
    """
    Метод для редактирования записей в справочнике
    :return: 
    """""

def find_by_sirname(sirname):
    """
    Метод для поиска записи в справочнике по фамилии
    :param sirname: фамилия
    :return:
    """

def find_by_name(name):
    """
    Метод для поиска записи в справочнике по имени
    :param name: имя
    :return:
    """

def find_by_patronym(patronym):
    """
    Метод для поиска записи в справочнике по отчеству
    :param patronym: отчество
    :return:
    """

def find_by_organization_name(organization_name):
    """
    Метод для поиска записи в справочнике по имени организации
    :param organization_name: имя организации
    :return:
    """


def find_by_work_phone(work_phone):
    """
    Метод для поиска записи в справочнике по рабочему телефону
    :param work_phone: рабочий телефон
    :return:
    """

def find_by_personal_phone(personal_phone):
    """
    Метод для поиска записи в справочнике по личному телефону
    :param personal_phone: личный телефон
    :return:
    """