print('''Let's play a game!
Wanna play?
Answer in yes or no by entering [Y/N] or [y/n]''')
answer=input()
sum1=0
if answer=='y' or answer=='Y':
	print("Think any number between 1 to 31 and then press 'd' or 'D' when done")
	a=input()
	if a=='d' or a=='D':
		print('''	Is the number present in this series of numbers?

			16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31

			if yes press 1 else press 0''')

	b=int(input())
	if b==1:
		sum1=2**4

	elif b==0:
		print("No problem")
	else:
		print("Wrong input entered")




	print('''	Is the number present in this series of numbers?


			8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31

			if yes press 1 else press 0''')

	b=int(input())
	if b==1:
		sum1=sum1+(2**3)
	elif b==0:
		print("No problem")
	else:
		print("Wrong input entered")


	print('''Is the number present in this series of numbers?

			4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31

			if yes press 1 else press 0''')

	b=int(input())
	if b==1:
		sum1=sum1+(2**2)
	elif b==0:
		print("No problem")
	else:
		print("Wrong input entered")

	print('''Is the number present in this series of numbers?
			2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31

			if yes press 1 else press 0''')

	b=int(input())
	if b==1:
		sum1=sum1+(2)
	elif b==0:
		print("No problem")
	else:
		print("Wrong input entered")

	print('''Is the number present in this series of numbers?
			1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31

			if yes press 1 else press 0''')

	b=int(input())
	if b==1:
		sum1=sum1
	elif b==0:
		print("No problem")
	else:
		print("Wrong input entered")

	print("Your entered number is")
	print(sum1)
	print('''Hehe Surprised!
Thanks for playing''')
else:
	print("Ok Thanks!")

		

