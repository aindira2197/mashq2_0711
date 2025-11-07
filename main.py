#1 - misol
def reverse_list(lst):
    return lst[::-1]

numbers = list(map(int, input("Raqamlarni probel bilan kiriting: ").split()))
print("Teskari ro‘yxat:", reverse_list(numbers))

#2 - misol
def calculator(a, b, amal):
    if amal == '+':
        return a + b
    elif amal == '-':
        return a - b
    elif amal == '*':
        return a * b
    elif amal == '/':
        return a / b if b != 0 else "0 ga bo‘lish mumkin emas"
    else:
        return "Noto‘g‘ri amal!"

a = float(input("Birinchi son: "))
b = float(input("Ikkinchi son: "))
amal = input("Amalni kiriting (+, -, *, /): ")
print("Natija:", calculator(a, b, amal))

#3 - misol
def word_count(s):
    return len(s.split())

s = input("Satr kiriting: ")
print("So‘zlar soni:", word_count(s))

#4 - misol
def double_even(lst):
    return [x * 2 if x % 2 == 0 else x for x in lst]

numbers = list(map(int, input("Raqamlarni probel bilan kiriting: ").split()))
print("Natija:", double_even(numbers))

#5 - misol
def dict_keys(d):
    return list(d.keys())

my_dict = {}
n = int(input("Nechta juftlik kiritasiz? "))
for i in range(n):
    key = input(f"{i+1}-kalitni kiriting: ")
    value = input(f"{i+1}-qiymatni kiriting: ")
    my_dict[key] = value

print("Kalitlar ro‘yxati:", dict_keys(my_dict))
