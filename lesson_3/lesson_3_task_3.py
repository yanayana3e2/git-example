from address import Address
from mailing import Mailing

# Создаем адреса
to_addr = Address("603159", "Нижний Новгород", "Акимова", "53", "30")
from_addr = Address("107564", "Москва", "Богатырская", "7", "123")

# Создаем почтовое отправление
mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=150,
    track="RB123456789CN"
)

# Проверяем данные
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")