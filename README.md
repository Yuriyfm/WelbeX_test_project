# WelbeX_test_project
Задание - https://faint-adasaurus-4bc.notion.site/web-Python-adf33211e9cc4d6b9ec2c0c619ecab31

## Выполнено:

* Таблица содержит 4 колоноки
* Использована база данных PostgreSQL
* Таблица имеет сортировку по всем полям кроме даты. 
* Фильтрация реализована в виде двух выпадающих списков и текстового поля:
  1) Выбор колонки, по которой будет фильтрация
  2) Выбор условия (равно, содержит, больше, меньше)
  3) Поле для ввода значения для фильтрации
* Таблица содержит пагинацию

## Не выполнено:

Вся таблица должна работать без перезагрузки страницы
Причина:
не удалось настроить работу ajax с сохранением корректной работы пагинации

##Примечание:

Исходя из содержания столбцов логика фильтации реализована следующим образом:
Функции фильтрации "Больше", "Меньше", не работают с полем "Название"
Функция фильтрации "Содержит", не работает с полями "Количество" и "Расстояние"

**ВАЖНО! Для начала работы, в файле settings.py, требуется указать параметры подключения к базе PostgreSQL**
