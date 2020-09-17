#!/usr/bin/env python3

import sys

number = round(float(sys.argv[1])) 

if number < 0:
	print(number, "é negativo")
elif number == 0:
	message = "igual a zero"
	print(number, message)
else:
	message = "é positivo"
	print(number, message)
	if number < 50:
		if(number % 2) == 0:
			print(number, "é menor que 50 e é par")
		else:
			print(number, "é menor que 50 e é impar") 
	else: 
		if(number%3) == 0:
			print(number, "é maior que 50 e é divisivel por 3")
		else:
			print(number, "é maior que 50 e não é divisivel por 3")
