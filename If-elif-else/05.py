# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#              Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)

print("Calculate Your Electricity bill Just Enter Your electricity Units ")

amt = 0
num = int(input("Enter the Number of  Uses Electricity  Units :  "))

if(num<=100):
    amt = "0Rs- No charge"
elif(num>100):
    amt = (num-100)*5
elif(num>=200):
    amt = 500+(num-200)*10
elif(num>=350):
    amt = "total bill Rs2000"

print("Amount is ",str(amt))

    
# For not close immediately 
input("Press Enter to close program")
