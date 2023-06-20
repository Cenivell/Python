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
num_of_participation = int(input("Number of people? "))
#Число днів в поході
duration_days = int(input("Amount of days? "))
#Змінна щоб ножів було не мешне двох на похід
knifes = num_of_participation/2
if knifes <= 2:
    knifes = 2
#Словник
trip_dict = {
    'Backpacks' : 1 * num_of_participation,
    'Raincoats' : 1 * num_of_participation,
    'Sleeping_bags' : 1 * num_of_participation,
    'Carpets' : 1 * num_of_participation,
    'Tents' : math.ceil(1 * num_of_participation/3), #Використав бібліотеку math для того щоб закругляти до найбільшного числа щоб всі жили в палатках
    'Cauldrons' : 1,
    'Bowls' : 1 * num_of_participation,
    'Knifes' : round(knifes), #Закругляю змінну
}
#Вивожу данні в консоль
print ('Amount of backpacks -',trip_dict['Backpacks'])
print ('Amount of raincoats -',trip_dict['Raincoats'])
print ('Amount of sleeping bags -',trip_dict['Sleeping_bags'])
print ('Amount of carpets -',trip_dict['Carpets'])
print ('Amount of tents -',trip_dict['Tents'])
print ('Amount of cauldrons -',trip_dict['Cauldrons'])
print ('Amount of bowls -',trip_dict['Bowls'])
print ('Amount of knifes -',trip_dict['Knifes'])
