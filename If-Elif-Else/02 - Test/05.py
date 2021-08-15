# Write a program to accept a number from 1 to 12 and display name of the month and days in 
# that month like 1 for January and number of days 31 and so on


print("Accept a number from 1 to 12 and display name of days and date ")

num=int(input("Enter any number between 1 to 7 : "))
if num==1:
    print("January")
elif num==2:
    print("February")
elif num==3:
    print("March")
elif num==4:
    print("April")
elif num==5:
    print("May")
elif num==6:
    print("June")
elif num==7:
    print("July")
elif num==8:
    print("August")
elif num==9:
    print("September")
elif num==10:
    print("October")
elif num==11:
    print("November")
elif num==12:
    print("December")
else:
    print("Please enter number between 1 to 12")


# For not close immediately 
input("Press Enter to close program")