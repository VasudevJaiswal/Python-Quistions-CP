# Write a program to check whether the last digit of a number( entered by user ) is 
# divisible by 3 or not.

print("Last Digit of Number is divisible by 3 or not ")

num = int(input("Enter Any Number"))
id = num%10     # If quis  says last digit so use %10

if(id%3==0):
    print("Last digit of number is divisible by 3")
else:
    print("Last digit of number is ''Not' divisible by 3")