# Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 
# 2 for Monday and so on.

print("Accept a Number from 1 to 7 to display Sun-Sat")

num = int(input("Enter Your number 1 to 7 : "))
if(num==1):
    print("Sunday")
elif(num==2):
    print("Monday")
elif(num==3):
    print("Tuesday")
elif(num==4):
    print("Wednesday")
elif(num==5):
    print("Thursday")
elif(num==6):
    print("Friday")
elif(num==7):
    print("Saturday")
else:
    print("Please Enter between 1 to  7 ")



# For not close immediately 
input("Press Enter to close program")