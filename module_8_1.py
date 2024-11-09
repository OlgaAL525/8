def add_everything_up(a, b):
    try:
        c = a + b
    except TypeError:
        if type (a) != str:
            c = str(a) + b
        elif type (b) != str:
            c =  a + str(b)
    return c



print(add_everything_up('a', 25))
print(add_everything_up(4, 25))
print(add_everything_up('кошка ', 'Мурка'))
print(add_everything_up(4.3, ' кг'))

