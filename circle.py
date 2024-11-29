import math

def area(r):
    '''
    Возвращает площадь окружности.
    
        Параметры:
            r (int): Радиус окружности

        Возвращаемое значение:
            circleArea (int): Плошадь окружности радиуса r
    
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности.
    
        Параметры:
            r (int): Радиус окружности

        Возвращаемое значение:
            circlePerimeter (int): Длина окружности радиуса r
    
    '''
    return 2 * math.pi * r
