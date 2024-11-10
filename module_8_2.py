def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    i = 0
    if type(numbers) == set:
        numbers = list(numbers)
    while i < len(numbers):
        try:
            result += numbers[i]
        except TypeError:
            incorrect_data += 1
        i += 1
    return (result, incorrect_data)


def clculate_average(numbers):
    try:
        s = round((personal_sum(numbers)[0]/(len(numbers)-personal_sum(numbers)[1])),2)
    except ZeroDivisionError:
        s = 0
    except TypeError:
        print('В nambers записан некорректный тип данных')
        s = None
    return s



print(clculate_average(3))
print(clculate_average('3'))
print(clculate_average({1, '6', 9}))
print(clculate_average([3, 7, 9]))
print(clculate_average((3, 'Кошка Мурка', 9)))