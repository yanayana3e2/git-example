from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        """
        Конструктор класса Mailing (почтовое отправление)
        
        Args:
            to_address (Address): Адрес получателя
            from_address (Address): Адрес отправителя  
            cost (int): Стоимость отправления
            track (str): Трек-номер
        """
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track