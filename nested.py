#nested loop = A loop within another loop(outer, inner)

#ex-1===========================


#for x in range(3):
	#for y in range(1,10):
		#print(y, end="")
	#print()


#ex-2==========================


#squar and rectag\ngle with the help of forloop

row = int(input("enter number for rows: "))
cloum = int(input("enter number for cloum: "))
symbol = input("enter the symbol")

for x in range(row):
	for y in range(cloum):
		print(symbol,end="")
	print()