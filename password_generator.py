import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword secure password Generator!")
num_of_letters= int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input(f"How many symbols would you like?\n"))
num_of_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy pasword - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easy_password = ""
for i in range(1, (num_of_letters + 1)):
  letter = letters[random.randint(1, 51)]
  easy_password += letter

for j in range(1, (num_of_symbols + 1)):
  symbol = symbols[random.randint(1, 8)]
  easy_password += symbol


for k in range(1, (num_of_numbers + 1)):
  number = numbers[random.randint(1, 9)]
  easy_password += number

print(f"Your easy password is {easy_password}")


#secure password - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []
for i in range(1, (num_of_letters + 1)):
  letter = letters[random.randint(1, 51)]
  password.append(letter)

for j in range(1, (num_of_symbols + 1)):
  symbol = symbols[random.randint(1, 8)]
  password.append(symbol)


for k in range(1, (num_of_numbers + 1)):
  number = numbers[random.randint(1, 9)]
  password.append(number)


random.shuffle(password)
password = ''.join(password)
print(f"Your most secure password is {password}")
