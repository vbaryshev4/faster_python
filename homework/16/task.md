## Задание: 
Есть бесконечная плоскость, по которой можно двигаться в 8 направлениях: 
```
из (x,y) в
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
```
Также есть последовательность точек, каждую из которых нужно посетить в том же порядке, в котором они даны.
Нужно посчитать минимальное количество шагов, за которое можно их все посетить, начиная с первой.

Пример:
```
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
```

Мы потратим 1 шаг (0, 0) из (1, 1), а потом еще один из (1, 1) в (1, 2).
