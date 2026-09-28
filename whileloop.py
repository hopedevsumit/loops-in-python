# while loop = execute some code WHILE some conditiom remains true


#name = input("Enter your name: ")
#1========================================


#while name == "":
	#print ("you did not enter your name")
	#name = input("Enter your name: ")
#print(f"hello{name}")



#2=======================================

#age = int(input("Enter your age: "))

#while age <0:
#	print("this is not vaild")
#	age = int(input("Enter your age: "))
#print(f"your are {age} year old")


#3=====================================

#food = input ("enter a food you like (q to quit): ")
#while not food =="q":
#	print(f"you like {food}")
#	food = input ("enter a food you like (q to quit): ")
#print("bye")



#4========================================

num = int(input("Enter your number between 1-10: "))

while num <1 or num >10:
	print(f"{num} is not vaild")
	num = int(input("Enter your number between 1-10: "))
print(f"you chose this {num}")