#  Write a program to check whether an years is leap year or not.

print("Check Years is Leep year or not")

year = int("Enter your Year : ")
if(year%100==0):
    if(year%400==0):
        print("Entered Year is Leep year")