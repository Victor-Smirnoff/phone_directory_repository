from DAO_phone_directory_repository import PhoneDirectoryRepository
from handler import Handler
from model import PhoneDirectoryModel
from error_response import ErrorResponse
from custom_error import PageError, LineError
from router import Router


phone_directory_obj = PhoneDirectoryRepository()
handler_obj = Handler()
router = Router()

print('Приветствую Вас на реализации телефонного справочника!')
print()
while True:
    print('Вывод постранично записей из справочника на экран - напишите цифру 1')
    print('Добавление новой записи в справочник - напишите цифру 2')
    print('Возможность редактирования записей в справочнике - напишите цифру 3')
    print('Поиск записей по одной или нескольким характеристикам - напишите цифру 4')
    print('Если хотите выйти из программы - напишите что угодно или не пишите вообще ничего')
    print()
    answer = input('Введите цифру 1, 2, 3 или 4 для работы со справочником: ')

    if answer not in ('1', '2', '3', '4'):                  # Если ответ пользователя не 1-2-3-4, то выходим из цикла и завершаем программу
        break

    handler_obj = router.determine_handler_method(answer)   # Используем роутер для выбора функции-обработчика
    handler_obj()                                           # Вызываем функцию-обработчик


print()
print('Спасибо за Ваш выбор! До новых встреч!')