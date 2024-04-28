import json

#создание словаря с текущими участниками группы
road_map = [
    {"дни выполнения": "1", "тема": 'установка python и IDE, первая программа "Hello World!"'},
    {"дни выполнения": "(2,3)", "тема": 'основа синтаксиса: переменные, базовые типы данных(int, float, str)'},
    {"дни выполнения": "(4,5)", "тема": 'операторы: арифметические,сравнение, логические'},
    {"дни выполнения": "(6,7)", "тема": 'практические задания на переменные и операторы'},
    {"дни выполнения": "(8,9)", "тема": 'условные операторы: if, elif, else'},
    {"дни выполнения": "(10,11)", "тема": 'Циклы: while, for, break, continue'},
    {"дни выполнения": "(12,13,14)", "тема": 'практические задания на условия и циклы'},
    {"дни выполнения": "(15,16,17)", "тема": 'списки (list) и операции с ними'},
    {"дни выполнения": "(18,19,20)", "тема": 'Словари (dictionaries) и множества (set)'},
    {"дни выполнения": "(21,22,23)", "тема": 'Кортежи (tuple) и их особенности'},
    {"дни выполнения": "(24,25,26,27,28)", "тема": 'практические задания на структуры данных'},
    {"дни выполнения": "(29,30,31)", "тема": 'Определение функций, возвращаемые значения, параментры, аргументы'},
    {"дни выполнения": "(32,33,34)", "тема": 'Область видимости переменных, локальные и глобальные переменные'},
    {"дни выполнения": "(35,36,37)", "тема": 'Импортирование модулей, создание своих модулей'},
    {"дни выполнения": "(38,39,40,41,42)", "тема": 'практические задания на функции и модули'},
    {"дни выполнения": "(43,44,45)", "тема": 'Классы и объекты, атрибуты и методы'},
    {"дни выполнения": "(46,47,48)", "тема": 'Наследование, полиморфизм и инкапсуляция'},
    {"дни выполнения": "(49,50,51)", "тема": 'Специальные методы класса (например, __init__ и __str__)'},
    {"дни выполнения": "(52,53,54,55,56)", "тема": 'Практические задания на ООП'},
    {"дни выполнения": "(57,58)", "тема": 'Основы исключений, блоки try и except'},
    {"дни выполнения": "(59,60)", "тема": 'создание собственных исключений'},
    {"дни выполнения": "(61,62,63)", "тема": 'практические задания на исключения и обработку ошибок'},
    {"дни выполнения": "(64,65,66,67,68,69,70)", "тема": 'Создание небольших проектов для закрепления материала'},
    {"дни выполнения": "(71,72,73,74,75,76,77)", "тема": 'Основы SQL и баз данных'},
    {"дни выполнения": "(78,79,80,81,82)", "тема": 'практические задачи по SQL'},
    {"дни выполнения": "(83,84)", "тема": 'Введение в Git, основные понятия (репозитории, ветки, коммиты). Установка '
                                          'Git. Настройка Git'},
    {"дни выполнения": "(85,86,87)", "тема": 'Основы работы с репозиториями. Создание нового репозитория и '
                                             'клонирование существующего. Использование базовых команд'},
    {"дни выполнения": "(88,89)", "тема": 'Консепция ветвления Git. Создание, перемещение и удаление веток, с помощью '
                                          'git branch, git checkout, git merge, git branch -d. Разрешение конфликтов '
                                          'при слиянии'},
    {"дни выполнения": "90", "тема": 'Дополнительные возможности Git. Продвинутые команды: Git stash, '
                                     'git cherry-pick, git rebase. Использование .gitignore для исключения файлов из '
                                     'репозитория'},
]

#запись словаря в файл
with open("road_map.json", "w") as file:
    json.dump(road_map, file)