import string
import random

alphabet_list = list(string.ascii_letters)

special_char_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
 ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

number_alphabet = int(input("Enter the number of alphabet you want : \n"))
number_char = int(input("Enter the number of character : \n"))
number_number = int (input("Enter the number of numbers : \n"))

sum = number_alphabet + number_char + number_number
print(f"generating your {sum} password......... \n password generated sucessfully!\n")

password_list = []

for alphabet in range(0,number_alphabet):
    password_list.append(random.choice(alphabet_list))

for special in range(0,number_char):
    password_list.append(random.choice(special_char_list))

for num in range(0,number_number):
    password_list.append(random.choice(number_list))

random.shuffle(password_list)
password = ""

for i in password_list:
    password += i

print(f"your password is : {password}")
