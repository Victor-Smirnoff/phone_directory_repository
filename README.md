## Реализация телефонного справочника со следующими возможностями:
1. Вывод постранично записей из справочника на экран
2. Добавление новой записи в справочник
3. Возможность редактирования записей в справочнике
4. Поиск записей по одной или нескольким характеристикам
### Особенности программы:
1. Реализация интерфейса через консоль (без веб- или графического интерфейса)
2. Хранение данных организовано в виде текстового файла, формат csv
3. В справочнике хранится следующая информация: id, фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)

### Для запуска программы:
1. Запустить файл main.py
   <br>
3. Выбрать операцию для выполнения, их предусмотрено 4:
   <br>
   1 - вывод записей на экран,
   <br>
   2 - добавление новой записи,
   <br>
   3 - редактирование записи,
   <br>
   4 - поиск записи.
   
4. После выполнения одной из операций, её можно выполнить ещё раз с другими входными параметрами. А также можно выполнить другую операцию по выбору.
### Подроднее о каждой операции:
#### Вывод постранично записей из справочника на экран
<b>В главном меню введите цифру 1.</b><br>
Будет предложено ввести номер страницы телефонного справочника - введите целое число с номером страницы.<br>
Будет предложено ввести максимальное количество записей на одной странице - введите целое число.<br>
Если запрос получился корректный, то в результате будет выведено в консоль найденное количество записей.<br>
А если запрос получился некорректный, то в результате будет выведено в консоль сообщение об ошибке.<br>

Дальше будет предложено ввести цифру 1 для повторения операции вывода записей на экран или любой другой символ для выхода в главное меню программы.<br>

#### Добавление новой записи в справочник
<b>В главном меню введите цифру 2.</b><br>
Будет сообщение "Для добавления новой записи в справочник необходимо ввести следующие данные"<br>
Введите фамилию:<br>
Введите имя:<br>
Введите отчество:<br>
Введите название организации:<br>
Введите телефон рабочий:<br>
Введите телефон личный (сотовый):<br>
Если результат записи успешный, то будет выведено сообщение: "Добавление новой записи в справочник выполнено успешно!"<br>
И после этого сообщения будет выведена записанная запись.<br>

После будет предложено "Для добавления новой записи в справочник - нажмите 2" или "Выйти в главное меню - напишите что угодно кроме цифры 2"

#### Возможность редактирования записей в справочнике
<b>В главном меню введите цифру 3.</b>

Будет выведено сообщение:<br>
Редактирование записей в справочнике<br>
Для редактирования записи в справочнике необходимо ввести айди записи<br>
Введите айди записи:<br>
После ввода айди записи будет выведено сообщение:<br>
Запись в справочнике с айди “id” найдена!<br>
Для редактирования одной характеристики в записи введите 1<br>
Для редактирования нескольких характеристик в записи введите 2<br>
Для выхода в главное меню введите что угодно кроме 1 и 2<br>
Введите параметр редактирования записи - число 1 или 2: <br>

<b>Далее если выбрать редактирование одной характеристики в записи число 1:</b><br>
Для редактирования записи в справочнике необходимо выбрать характеристику для изменения<br>
1 - изменить фамилию<br>
2 - изменить имя<br>
3 - изменить отчество<br>
4 - изменить название организации<br>
5 - изменить телефон рабочий<br>
6 - изменить телефон личный (сотовый)<br>
Для выбора характеристики для изменения введите одну из следующих цифр 1,2,3,4,5,6: <br>
Будет сообщение по типу:<br>
Введите "название характеристики" и после появится сообщение:<br>
Редактирование строки с айди: “id”<br>
Редактирование строки с айди: “id” прошло успешно!<br>
{“id”: “id”, “фамилия”: “фамилия”, “имя: “имя”, “отчество”: “отчество”, “название организации”: “название организации”, “телефон рабочий”: “телефон рабочий”, “телефон личный (сотовый)”: “телефон личный (сотовый)”}<br>

И выход в главное меню программы

<b>Далее если выбрать редактирование нескольких характеристик в записи число 2:</b><br>
Для редактирования записи в справочнике необходимо выбрать характеристику для изменения<br>
1 - изменить фамилию<br>
2 - изменить имя<br>
3 - изменить отчество<br>
4 - изменить название организации<br>
5 - изменить телефон рабочий<br>
6 - изменить телефон личный (сотовый)<br>
Для выбора характеристик введите через пробел следующие из цифр 1,2,3,4,5,6: <br>
Будет повторяться сообщение по типу:<br>
Введите "название характеристики"<br>
Для всех выбранных характеристик<br>
И после появится сообщение:<br>
Редактирование строки с айди: “id”<br>
Редактирование строки с айди: “id” прошло успешно!<br>
{“id”: “id”, “фамилия”: “фамилия”, “имя: “имя”, “отчество”: “отчество”, “название организации”: “название организации”, “телефон рабочий”: “телефон рабочий”, “телефон личный (сотовый)”: “телефон личный (сотовый)”}<br>

И выход в главное меню программы

#### Поиск записей по одной или нескольким характеристикам
<b>В главном меню введите цифру 4.</b>

Будет сообщение:<br>
Для поиска по одной характеристике напишите 1<br>
Для поиска по нескольким характеристикам напишите 2<br>
Для выхода напишите что угодно, кроме 1 и 2<br>

Введите 1 или 2:

После ввода цифры 1 будет сообщение:<br>
Поиск записей возможен по следующим характеристикам:<br>
1 - по айди записи<br>
2 - по фамилии<br>
3 - по имени<br>
4 - по отчеству<br>
5 - по названию организации<br>
6 - по телефону рабочему<br>
7 - по телефону личный (сотовый)<br>
Для выхода введите любой символ, отличный от цифр 1-7<br>
Для поиска введите одну из следующих цифр 1,2,3,4,5,6,7:<br>

После ввода любой цифры 1,2,3,4,5,6,7 будет предложено ввести выбранную характеристику для поиска.<br>
После ввода выбранной характеристики будет выведен результат поиска.

После ввода цифры 2 будет сообщение:<br>
Поиск записей возможен по следующим характеристикам:<br>
1 - по айди записи<br>
2 - по фамилии<br>
3 - по имени<br>
4 - по отчеству<br>
5 - по названию организации<br>
6 - по телефону рабочему<br>
7 - по телефону личный (сотовый)<br>
Для поиск записей по нескольким характеристикам введите числа от 1 до 7 через пробел:<br>
Для выхода введите любой нечисловой символ<br>
Для поиска введите через пробел следующие из цифр 1,2,3,4,5,6,7:<br>

После ввода любых цифр 1,2,3,4,5,6,7 через пробел будет предложено ввести выбранные характеристики для поиска.<br>
После ввода всех выбранных характеристик будет выведен результат поиска.
