class Address:
    def __init__(self, index, city, street, house, apartment):
        """
        Конструктор класса Address
        
        Args:
            index (str): Индекс
            city (str): Город
            street (str): Улица
            house (str): Дом
            apartment (str): Квартира
        """
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment