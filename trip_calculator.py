##########################
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
#Імпортую бібліотеку math
import math


#функції
def check_is_number(number: str or int):
    '''Функція для перевірки чи змінна є числом'''
    if isinstance(number, int) or isinstance(number, str) and number.isnumeric():
        pass
    else:
        exit("Please make sure that all values are integers")


def print_output_in_console(dictionary: dict,):
    '''Функція для виведення словника в консоль'''
    for key, value in dictionary.items():
        print(f'{key}: {math.ceil(value)}')


def add_amount_to_food_dictionary(current_dict: dict, x: dict) -> dict:
    '''Функція додавання кількості їди для числа'''
    for dictionary in [current_dict]:
        for key in dictionary.keys():
            if key in out_dict.keys():
                x[key] += dictionary[key]['amount'] * num_of_participation
            else:
                x.update({key: dictionary[key]['amount'] * num_of_participation})
    return x


#Приймаю вхідні данні та перевіряю чи вони є числом
num_of_participation = (input("Number of people? "))
check_is_number(num_of_participation)
num_of_participation = int(num_of_participation)

duration_days = (input("Amount of days? "))
check_is_number(duration_days)
duration_days = int(duration_days)

#Змінна щоб ножів було не мешне двох на похід
knifes = num_of_participation/2
if knifes <= 2:
    knifes = 2
#Змінна в якій множу число учасників на 3
multiply_people_by_3 = num_of_participation*3
#Змінна в яку записується загальна вага продуктів
total_food_weight = 0

#Словники:
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
trip_food_variation_1_dict = {
    'Чай карпатський "Чаїдло"': {
        'calories': 223,
        'water': 1000,
        'weight': 40,
        'amount': 0.2,
    },
    'Гранола горіхова з шоколадом': {
        'calories': 442,
        'water': 200,
        'weight': 100,
        'amount': 1,
    }, #calories - 442 water - 200 weight - 100
    'Харчо грузинське з яловичиною': {
        'calories': 187,
        'water': 350,
        'weight': 57,
        'amount': 1,
    }, #calories - 187 water - 350 weight - 57
    'Гречка з яловичиною': {
        'calories': 320,
        'water': 350,
        'weight': 100,
        'amount': 1,
    }, #calories - 320 water - 350 weight - 100
    'Батончик енергетичний OMNOM неспішне какао"': {
        'calories': 621,
        'water': 0,
        'weight': 150,
        'amount': 3,
    },  #calories-621 weight - 150(3 на день)
}
trip_food_variation_2_dict = {
    'Чай карпатський "Чаїдло"': {
        'calories': 223,
        'water': 1000,
        'weight': 40,
        'amount': 0.2,
    },
    'Каша бананова': {
        'calories': 456,
        'water': 200,
        'weight': 100,
        'amount': 1,
    }, #calories - 456 water - 200 weight - 100
    'Борщ з яловичиною та квасолею': {
        'calories': 160,
        'water': 350,
        'weight': 50,
        'amount': 1,
    }, #calories - 160 water - 350 weight - 50
    'Картопля з курячим філе': {
        'calories': 345,
        'water': 350,
        'weight': 90,
        'amount': 1,
    }, #calories - 345 water - 350 weight - 90
    'Батончик енергетичний  OMNOM крута журавлина"': {
        'calories': 674,
        'water': 0,
        'weight': 150,
        'amount': 3,
    },  #calories- 674 weight-150(3 на день)
}
trip_food_variation_3_dict = {
    'Чай карпатський "Чаїдло"': {
        'calories': 223,
        'water': 1000,
        'weight': 40,
        'amount': 0.2,
    },
    'Каша кукурудзяна з насінням чіа та маком': {
        'calories': 411,
        'water': 200,
        'weight': 100,
        'amount': 1,
    }, #calories - 411 water -200 weight - 100
    'Суп гороховий з яловичиною': {
        'calories': 185,
        'water': 350,
        'weight': 60,
        'amount': 1,
    }, #calories - 185 water - 350 weight - 60
    'Полента з яловичиною': {
        'calories': 329,
        'water': 350,
        'weight': 100,
        'amount': 1,
    }, #calories - 329 water - 350 weight - 100
    'Батончик енергетичний OMNOM заряджене еспресо" ': {
        'calories': 615,
        'water': 0,
        'weight': 150,
        'amount': 3,
    },  #calories-615 weight-150(3 на день)
}
out_dict = {
}
#Виписую данні в консоль
print('------------------Items------------------')
print_output_in_console(trip_items_dict)
print('----------------Products----------------')
#Вираховую кількість продуктів
x = 0; y = 0
prefix = "trip_food_variation_"; suffix = "_dict"
while x < duration_days:
    x += 1
    y += 1
    add_amount_to_food_dictionary(globals()[prefix + str(y) + suffix], out_dict)
    total_food_weight += sum(item.get('weight', 0) for item in globals()[prefix + str(y) + suffix].values())
    if y == 3:
        y = 0
#Виписую кількість продуктів в консоль
print_output_in_console(out_dict)
#Виписую вагу
total_food_weight *= num_of_participation
print("Total food weight is",int(total_food_weight),'mg.')
print("Food weight per person is",int(total_food_weight/num_of_participation),'mg.')
