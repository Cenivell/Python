###########################
# Опис завдання:
# Сворити розумнийкалькулятор для обрахування кількості потрібних речей та продуктів
# для походу у розрахунку на кількість осіб та тривалість походу.
#
# Розробка:
# У ході розробки калькулятора певні елемнети будуть уточнюватись, тому варто відразу думати про можливість розширення.
#
# Технічне завдання:
# Використати тільки python та вбудовані бібліотеки.
# Очікується для розрахунку 2 вхідних параметра:
# 1) Кількість учасників (num_of_participations): int
# 2) Триваліть у днях (duration_days): int
#
# Результатом роботи коду має бути вивід кожного елемента (специфікація елемнета та їх розрахунок -  у табличці нижче),
# у форматі dict : key=item, value=calculated.
#
# Таблиця розрахунків, що використовуються (у коді важливо використовувати назви англ. мовою):
# Предмет  |  Розрахунок         | Коммент
# рюкзак      1 / людина
# дощовик     1 / людина
# спальник    1 / людина
# коремат     1 / людина
# палатка     1 / 3 людей          всі мають жити у палатках
# казанок     1 / всіх
# миска       1 / людина
# ніж         1 / 2 людей          не менше 2 на похід, але розрахунок на 2 людей.
#
#

###########################
# Рішення нижче
###########################

#Імпортую бібліотеку
import math
#Число учасників походу
num_of_participation = (input("Number of people? "))
if num_of_participation.isnumeric():
    num_of_participation = int(num_of_participation)
else:
    print("Please redeem a integer")
    exit(1)
#Число днів в поході
duration_days = (input("Amount of days? "))
if duration_days.isnumeric():
    duration_days = int(duration_days)
else:
    print("Please redeem a integer")
    exit(1)
#Змінна щоб ножів було не мешне двох на похід
knifes = num_of_participation/2
if knifes <= 2: knifes = 2
#Словник
trip_dict = {
    'backpacks' : num_of_participation,
    'raincoats' : num_of_participation,
    'sleeping_bags' : num_of_participation,
    'carpets' : num_of_participation,
    #Використав бібліотеку math для того щоб закругляти до найбільшного числа щоб всі жили в палатках
    'tents' : math.ceil(1 * num_of_participation/3),
    'cauldrons' : 1,
    'bowls' : num_of_participation,
    'knifes' : round(knifes), #Закругляю змінну
}
#Вивожу данні в консоль
for key, value in trip_dict.items():
    print('Amount of', key, value)
