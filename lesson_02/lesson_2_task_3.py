import math


def square(side):
    area = side * side
    if isinstance(side, int):
        return area
    else:
        return math.ceil(area)
    print(square(5))
    print(square(2.5))
