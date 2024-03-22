def trapez(func, a, b, N):
    h = (b - a) / N
    integral = 0.5 * (func(a) + func(b))
    for i in range(1, N):
        integral += func(a + i * h)
        result = h * integral
        return round(result, 8)


def f(x):
    return x ** 2


result = trapez(f, 5, 7, 100)
print(result)
