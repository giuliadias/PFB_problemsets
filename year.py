#!/usr/bin/env python3

import sys 

year = float(sys.argv[1])

if(year % 4) == 0:
	if (year % 100) == 0: 
		print(year, "não é ano bissexto")
	else:
		print(year, "é um ano bissexto")
elif(year % 400) == 0:
	print(year, "é um ano bissexto")
else:
	print(year, "não eh ano bissexto")
