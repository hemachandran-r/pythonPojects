print("----------NAME---> HEMACANDRAN R ----------")
print("---------- BATCH NO--->74 ----------")
print("----------MOBILE NO--->6374944765----------")
print("----------COLLAGE--->GLOBAL INSTITUTE OF ENGINEERING AND TECHNOLOGY")
print("----------PLACE--->MALVISHARAM----------")
print("----------DISTRICR--->RANIPET----------")
print("*****************************************************")

print("\n")
print("*******************************************************")
print("\n\n$$$$$$$$$$$$$TICKET BOOKING SYSTEM$$$$$$$$$$$$$$$\n")
print("*******************************************************")
print("*******************************************************")
print("$$$$$$$$$$$$$$$$ VS BOOKING SYSTEM  $$$$$$$$$$$$$$$$$$$")



def main():

	print("1.Check PNR status")
	print("2.Ticket Reservation")
	p=int(input("enter your option: "))

	if p== 1:
		print("Your PNR status is t9")
		exit(0)

	elif p == 2:


		print("1-->ooty")
		print("2-->Bengaluru")
		print("3--->Kodaikanal")
		print("4--->vellore")
		L=int(input("enter your choiceL "))

		if L==1:
			
			print("ticket price--->2500")

			name=input("enter your name: ")

			age=int(input("enter your age: "))

			mobile_no=int(input("enter your mobile number: "))

			gender=input("enter your gender: ")

			print("1-->submit")

			print("2-->cancle")

			t=int(input("enter your choice: "))

			if t==1:

				print("your ticket is booked sucessfully")

				print("Thank You For Booking Happy Jurnoy")

			elif t==2:
			
				print("your ticket booking process is cancled")

				print("Thank You")

			
            
		if L==2:
			print("ticket price--->2000")

			name=input("enter your name: ")

			age=int(input("enter your age: "))

			mobile_no=int(input("enter your mobile number: "))

			gender=input("enter your gender: ")

			print("1-->submit")

			print("2-->cancle")

			h=int(input("enter your choise: "))

			if h==1:
				print("your ticket is booked successfully")

				print("Thank Your For Booking Happy jurnoy")

			elif h==2:
				print("your tickt booking process is cancled")	

				print("Thankyou")

		if L==3:
			print("ticket price---->1500")

			name=input("enter your name: ")

			age=int(input("enter your age: "))

			mobile_no=int(input("enter your mobile number"))

			gender=input("enter your gender")

			print("1-->submit")

			print("2-->cancle")

			k=int(input("enter your choiceL "))

			if k==1:
				print("your ticket is booked successfully")

				print("Thank You For Booking Happy Jurnoy")
			elif k==2:
				print("your ticket booking process is cancled")	

				print("Thank You For Booking ")

				   
main()

		 