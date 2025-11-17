rate_as_str = input("Оцените работу оператора: ")
rate = int(rate_as_str)

if(rate<1):
    rate = 1

if(rate > 5):
    rate = 5


feedback = ''

if rate == 1:
    feedback = input("что улучшить: ")
elif rate == 2:
    feedback = input("что случилось: ")
elif rate == 3:
    feedback = input("извинитесь: ")
elif rate == 4:
    feedback = input("поч не 5: ")
else:
    feedback = input("за что похвалить: ")

print(feedback)