#1.Функция с параметрами по умолчанию:

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params('List',7.01)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

#2.Распаковка параметров:

values_list = (21, True, 'Hi')
values_dict = {'a': False, 'b': 'While', 'c': 8.3}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:

values_list_2 = ('Picture', 2*2)
print_params(*values_list_2, 42)