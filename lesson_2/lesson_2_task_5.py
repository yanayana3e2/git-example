def month_to_season(month_number):
    if not isinstance(month_number, int) or not (1 <= month_number <= 12):
        return "Ошибка: номер месяца должен быть целым числом от 1 до 12."

    if month_number in (12, 1, 2):
        return "Зима"
    elif month_number in (3, 4, 5):
        return "Весна"
    elif month_number in (6, 7, 8):
        return "Лето"
    else: # 9, 10, 11
        return "Осень"
    
print(month_to_season(2))   # Ожидаемый вывод: Зима
print(month_to_season(4))   # Ожидаемый вывод: Весна
print(month_to_season(11))  # Ожидаемый вывод: Осень
print(month_to_season(0))   # Ожидаемый вывод: Ошибка: номер месяца должен быть целым числом от 1 до 12.
print(month_to_season(13))  # Ожидаемый вывод: Ошибка: номер месяца должен быть целым числом от 1 до 12.