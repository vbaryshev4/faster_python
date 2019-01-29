## Запросы с синонимами

Дано:
 - список пар синонимов
 - список пар запросов

Для каждой пары запросов нужно определить, являются ли они эквивалентными.
Эквивалентность определяется с точностью до синонимов.

С помощью уточняющих вопросов определили конкретный вариант задачи:
- порядок важен
- синонимичность транзитивна
- слова регистронезависимы
- все синонимы состоят из одного слова
- все слова содержат только маленькие буквы
- слова уже нормированы

Пример:
```
SYNONYMS = [
  ('rate', 'ratings'),
  ('approval', 'popularity'),
]

QUERIES = [
  ('obama approval rate', 'obama popularity ratings'),
  ('obama approval decline', 'obama popularity ratings'),
  ('obama approval rate', 'popularity ratings obama')
]
```
Вывод:
```
True
False
False
```

[Более подробный разбор этой задачи](https://medium.com/@alexgolec/google-interview-problems-synonymous-queries-36425145387c)
