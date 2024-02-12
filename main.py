from DAO_phone_directory_repository import PhoneDirectoryRepository
from router import Router


phone_directory_obj = PhoneDirectoryRepository()
router = Router()

def start_servicing():
    """
    Метод запускает цикл обслуживания всей программы
    :return: None
    """
    print('Приветствую Вас на реализации телефонного справочника!')
    print()git
    while True:
        print('Вывод постранично записей из справочника на экран - напишите цифру 1')
        print('Добавление новой записи в справочник - напишите цифру 2')
        print('Возможность редактирования записей в справочнике - напишите цифру 3')
        print('Поиск записей по одной или нескольким характеристикам - напишите цифру 4')
        print('Если хотите выйти из программы - напишите что угодно или не пишите вообще ничего')
        print()
        answer = input('Введите цифру 1, 2, 3 или 4 для работы со справочником: ')

        # Если ответ пользователя не 1-2-3-4, то выходим из цикла и завершаем программу
        if answer not in ('1', '2', '3', '4'):
            break

        handler_obj = router.determine_handler_method(answer)  # Используем роутер для выбора функции-обработчика
        handler_obj()  # Вызываем функцию-обработчик

    print()
    print('Спасибо за Ваш выбор! До новых встреч!')


if __name__ == '__main__':
    start_servicing()