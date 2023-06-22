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
    'backpacks' : 1 * num_of_participation,
    'raincoats' : 1 * num_of_participation,
    'sleeping_bags' : 1 * num_of_participation,
    'carpets' : 1 * num_of_participation,
    'tents' : math.ceil(1 * num_of_participation/3), #Використав бібліотеку math для того щоб закругляти до найбільшного числа щоб всі жили в палатках
    'cauldrons' : 1,
    'bowls' : 1 * num_of_participation,
    'knifes' : round(knifes), #Закругляю змінну
}
#Вивожу данні в консоль
for key, value in trip_dict.items():
    print('Amount of', key, value)