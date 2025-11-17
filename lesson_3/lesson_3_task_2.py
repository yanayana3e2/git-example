from smartphone import Smartphone

# Создаем переменную catalog - список смартфонов
catalog = [Smartphone("Samsung", "Galaxy S23", "+79123456789"), Smartphone("Apple", "iPhone 15 Pro", "+79234567890"),Smartphone("Xiaomi", "Redmi Note 13", "+79345678901"), Smartphone("Google", "Pixel 8", "+79456789012"), Smartphone("OnePlus", "11 Pro", "+79567890123")]

print("Каталог смартфонов:")
print("=" * 40)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")