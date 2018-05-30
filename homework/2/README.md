## Homework 02

#### Сортировка большого файла

Есть очень большой (не влезает в память) файл логов вида:
```
username email datetime
Вася Петров vp@mail.ru 2014-01-31 13:00
Коля Петров kp@mail.ru 2014-02-21 13:00
Ваня Петров vp2@mail.ru 2013-03-31 13:00
```

Требуется написать программу, которая может отсортировать этот файл по datetime.
Интерфейс программы:
```
merger.py [option] ... [PATH_TO_FILE]
```
Где возможные опции:
-n - количество воркеров,
-m - ограничение по памяти на одного воркера (в Kb).

Разделители в файле – табуляция. Ограничение по памяти трактуется
как общий размер логов в памяти.

Для тестирования предлагается сгенерировать тестовый файл с помощью ```test_generator.py```.
Он принимает на вход два файлв email.txt и names.txt. Emails можно взять из предыдущего задания, 
а имена получить, например, [здесь](http://freegenerator.ru/fio) (там можно выбрать только имя/фамилию).

Для начала предлагается реализовать один воркер.