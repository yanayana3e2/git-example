def bank(X, Y):
    """
    Расчет суммы вклада с капитализацией процентов
    
    Args:
        X (float): начальная сумма вклада
        Y (int): срок вклада в годах
    
    Returns:
        float: итоговая сумма на счету
    """
    amount = X
    for year in range(Y):
        amount += amount * 0.10
    return amount

if __name__ == "__main__":
    print("Вклад 1000 рублей на 3 года:")
    result1 = bank(1000, 3)
    print(f"Итоговая сумма: {result1:.2f} рублей")
    
    print("\nВклад 5000 рублей на 5 лет:")
    result2 = bank(5000, 5)
    print(f"Итоговая сумма: {result2:.2f} рублей")
    
    print("\nВклад 10000 рублей на 10 лет:")
    result3 = bank(10000, 10)
    print(f"Итоговая сумма: {result3:.2f} рублей")