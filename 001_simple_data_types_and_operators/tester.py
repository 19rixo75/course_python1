# number = 500         # integer - int
# number2 = 500.0      # float
# text_string = 'Hello'  # string - str
# text_string1 = "Hello"
# text_string2 = '''Hello'''
# text_string3 = """Hello"""
# text_string4 = "thet's"
# boolean_var = True     # boolean - bool
# boolean_var1 = False
# none_type = None       # None type
# print(number)
# print(type(number))
# print(type(number2))
# print(type(text_string))
# print(type(boolean_var))

# a = 500
# b =600
# result = a / b
# print(result)
# print(int(result))

# a = 10
# b = 20
# print(a > b)

# user_input = input('Please enter your salary: ')
# print(user_input)

# a = 0
# b = 2.5
# bool_var = False
# text_string = 'Hello'
# none_var = None
#
# print(a, b, bool_var, text_string, none_var)

# name = 'Dima'
# age = 45
#
# print('Hello ' + name + ' you are ' + str(age) + ' ' + 'old')

# a, b, c = input('Please enter: ').split()   # split() способ определения разделения введенных значений (', ')
# print(a)
# print(b)
# print(c)
# площадь треугольника по трем сторонам
# a, b, c = input('Please enter sides A, B, and C. Use space separator').split()
# half_perimeter = (int(a) + int(b) + int(c)) / 2
# triangle_area = (half_perimeter * (half_perimeter - int(a)) * (half_perimeter - int(b)) * (half_perimeter - int(c))) ** 0.5
# print(triangle_area)

# \t табуляция - 4 пробела
# \n перенос строки
# \ игнорирует символ

# exponent
a, n = input('Please enter sides A - number, B - exponent. Use space separator: ').split()
result = pow(int(a), 1/int(n))
print(result)


