# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
#         Cost price (in Rs)                                       Tax
#         > 100000                                                  15 %
#         > 50000 and <= 100000                          10%
#         <= 50000                                                  5%


print("By Cost price of a bike - calculate  road tax to be paid ")

tax = 0
Cost_Price = int(input("Enter Cost price of Bike : "))

if(Cost_Price>100000):
    tax = (Cost_Price*15)/100
elif(Cost_Price>50000 and Cost_Price<=100000):
    tax = (Cost_Price*10)/100
elif(Cost_Price<=50000):
    tax = (Cost_Price*5)/100

# For not close immediately 
input("Press Enter to close program")