print("\n\nTicket Booking System\n")
restart = ('Y')

while restart != ('N','NO','n','no'):

	print("1.Total number of seats")
	print("2.Ticket Reservation")
	print("3.Current available seat: ")

	option = int(input("\nEnter your option : "))

	if option == 1:
		print("The seat status is ", 4)
		exit(0)



	elif option == 2:
		people = int(input("\nTicket reservation on remaining seats : "))
		trainname_l = []
		age_l = []
		sex_l = []
		for p in range(2):
			trainname = str(input("\nTrain Name : "))
			trainname_l.append(trainname)
			age  = int(input("\nAge  : "))
			age_l.append(age)
			sex  = str(input("\nMale or Female : "))
			sex_l.append(sex)


		restart = str(input("\nDid you forgot someone? y/n: "))
		if restart in ('y','YES','yes','Yes'):
			restart = ('Y')
		else :
			x = 0
			print("\nTotal Seats : ",2)
			for p in range(1,people+1):
				print("Ticket : ",p)
				print("Name : ", trainname_l[x])
				print("Age  : ", age_l[x])
				print("Sex : ",sex_l[x])
				x += 1

	elif option==3:
		print('Seat availble right now is:', 2)