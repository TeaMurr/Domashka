name = "Тимур "
print(name)
age = "19"
print("Меня зовут", name, "и мне", age,"лет")
name5 = name*5
print(name5)
user_name = input("Как тебя зовут?")
user_age = input("Сколько тебе лет?")
user_age=int(user_age)
if user_age < 25:
    print("Привет", user_name, ".", "Тебе", user_age, "лет?..А где твоя мама, малыш?")
else:
    print("Привет", user_name, ".", "Тебе", user_age, "лет?.. Ох, так столько моей бабушке лет!")
user_name = str(user_name)
print(user_name[1:-1:1])
print(user_name[::-1])
print(user_name[-3::1])
print(user_name[:5:1])
length_of_user_name =len(user_name)
p = 1
summ = 0
user_age = int(user_age)
while (user_age != 0):
    summ = summ + (user_age % 10)
    p = p * (user_age % 10)
    user_age = user_age // 10
print("Длина Имени:", length_of_user_name,"Сумма цифр возраста:",summ,"Произведение цифр",p)
quest = input("Сколько будет 2+2?")
if (quest != 4):
    print("Неверно:(")
else:
    print("Верно:]")
