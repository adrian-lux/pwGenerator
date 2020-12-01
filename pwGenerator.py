#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
string_letters= input("How many letters would you like in your pw? (8)\n" )
if(string_letters):
  nr_letters=int(string_letters)
else:
  nr_letters=8

string_symbols = input(f"How many symbols would you like? (2)\n")
if(string_symbols):
  nr_symbols = int(string_symbols)
else:
  nr_symbols=2


string_numers = input(f"How many numbers would you like? (2)\n")
if(string_numers):
  nr_numbers = int(string_numers)
else:
  nr_numbers = 2

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
passwordList = []
for letter in range(1,nr_letters+1):
 passwordList.append(random.choice(letters))

for letter in range(1,nr_symbols+1):
 passwordList.append(random.choice(symbols))

for letter in range(1,nr_numbers+1):
 passwordList.append(random.choice(numbers))

random.shuffle(passwordList)
password = ''
for char in passwordList:
  password += char

print("Your pw is:")
print(password)
