def valume(a, b, c=None):
    if c is None:
        return a * b # площадь прямоугольника
    else:
        return a * b * c # обьем параллелепипеда
print(valume(2,3))
print(valume(2, 2, 2))