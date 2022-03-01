def greater(x, y):
    if x > y:
        return x
    else:
        return y


def greatest(x, y, z):
    bigger = greater(x, y)
    return greater(bigger, z)


print(greatest(30, 34, 21))
