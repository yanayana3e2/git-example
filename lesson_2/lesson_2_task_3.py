import math

def square(side):
  if side != int(side):  # Проверяем, является ли сторона целым числом
    return math.ceil(side * side)
  else:
    return side * side
print(square(5))
print(square(5.5))
print(square(4.2))
print(square(3))