###########################
# Опис завдання:
#
# Сворити розумнийкалькулятор для обрахування кількості потрібних речей та продуктів
# для походу у розрахунку на кількість осіб та тривалість походу.
#
# Розробка:
# У ході розробки калькулятора певні елемнети будуть уточнюватись, тому варто відразу думати про можливість розширення.
#
# Частина 1
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
# Частина 2: Розрахунок продуктів.
# Відомо, що на день одній людині потрібно ~2200 кіло-калорій, щоб комфортно почуватися.
# Продукти поході повинні довго зберігатися та бути герметично закритими, бажано без залишків із попреднього дня.
# Також під час походу важливо зберігати питний режим, тому потрібно вдень вживати ~2 літри води.

# Технічне завдання:
# Попередні розрахунки зберігаються.
# Вхідні параметри ті ж самі.
# Ваажається, що протягом дня учасники харчуюються 3 рази:
# - сндіанок - каша / м'ясо
# - обід - бутерброд / енергетичний батончик
# - вечеря - суп на основі готових брекетів з овочами
# Важливо! Компоненти мають змінюватись кожен день і повторюватися не часиіше ніж раз на 3 дні.
# 
# Результатом роботи коду має бути:
# 1) Розрахунок продуктів, потрібних на вказану кількості денів та осіб.
# 2) Розрахунок ваги продуктів загалом
# 3) Розрахунок ваги продукті з розподілом на кожного учасника походу.


# Результатом роботи коду має бути вивід кожного елемента,у форматі dict : key=item, value=calculated,
# та вказано вагу на 1 особу / на всіх осіб.

###########################
# Рішення нижче
###########################
#Функція для перевірки чи змінна є числом
def check_is_number(number: str or int):
    if isinstance(number, int) or isinstance(number, str) and number.isnumeric():
        pass
    else:
        exit("Please make sure that all values are integers")
#Імпортую бібліотеку
import math
#Число учасників походу
num_of_participation = (input("Number of people? "))
#Викликаю функцію
check_is_number(num_of_participation)
#Конвертую в інту
num_of_participation = int(num_of_participation)
#Число днів в поході
duration_days = (input("Amount of days? "))
#Викликаю функцію
check_is_number(duration_days)
#Конвертую в інту
duration_days = int(duration_days)
#Змінна щоб ножів було не мешне двох на похід
knifes = num_of_participation/2
if knifes <= 2: knifes = 2
#Словник
trip_items_dict = {
    'backpacks': num_of_participation,
    'raincoats': num_of_participation,
    'sleeping_bags': num_of_participation,
    'carpets': num_of_participation,
    #Використав бібліотеку math для того щоб закругляти до найбільшного числа щоб всі жили в палатках
    'tents': math.ceil(num_of_participation/3),
    'cauldrons': 1,
    'bowls': num_of_participation,
    'knifes': round(knifes), #Закругляю змінну
}
#Щоб не робити повторювальну дії вивожу в змінну
multiply_people_by_days=num_of_participation*duration_days
#Словник для продуктів
trip_food_dict = {
    'Гранола горіхова з шоколадом': multiply_people_by_days, #calories - 442 water -200 weight -100
    'Харчо грузинське з яловичиною': multiply_people_by_days, #calories - 187 water - 350 weight - 57
    'Гречка з яловичиною': multiply_people_by_days, #calories - 320 water - 350 weight - 100
    'Чай карпатський "Чаїдло"': multiply_people_by_days, #calories - 213 water - 1000 weight - 40
    'Чай карпатський "Чаїдло"': multiply_people_by_days, #calories - 458 weight - 100
    'Батончик енергетичний OMNOM неспішне какао"': multiply_people_by_days * 3,  #calories - 621 weight - 150(3 на день)
}
#Список ваги продуктів
food_weight_list=[100,57,100,40,100,450]
#Загально вага продуктів
total_food_weight=multiply_people_by_days*sum(food_weight_list)
#Вага на людину
food_weight_per_person=total_food_weight/num_of_participation
#Вивожу данні в консоль
print('------------------Items------------------')
for key, value in trip_items_dict.items():
    print('Amount of', key, value)
print('----------------Products----------------')
for key, value in trip_food_dict.items():
    print('Amount of', key, value)
print("Total food weight is",total_food_weight)
print("Food weight per person is",int(food_weight_per_person))
