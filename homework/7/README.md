## Homework 07

#### LRU Cache

Реализовать LRU (Least Recently Used) кэш. 

Класс LRUCache при инициализации получает n -- размер кэша и должен содержать два публичных метода: 

- set(key, value) добавляет значение value по ключу key. Общий размер кэша не должен превысить n. 
Для этого нужно удалять наиболее давно использованные ключи, когда кэш достигнет размера n.
- get(key) возвращает value, соответствующее данному ключу.

Обе операции должны иметь сложность O(1).