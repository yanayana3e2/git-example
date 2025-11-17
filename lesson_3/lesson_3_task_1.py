from user import User

# Создаем экземпляр User и сохраняем в переменную my_user
my_user = User("Marta", "Evgenevna")

# Вызываем все методы у объекта my_user
print("Вызов метода print_first_name:")
my_user.print_first_name()

print("\nВызов метода print_last_name:")
my_user.print_last_name()

print("\nВызов метода print_full_name:")
my_user.print_full_name()