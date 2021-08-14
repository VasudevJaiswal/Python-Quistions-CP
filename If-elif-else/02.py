# Write a program to check whether a number entered by user is even or odd.

print("Enter your Number to Check Even or Odd ")

num = int(input("Enter the Number : "))
if num%2==0:
    print("Number is Even")
else:
    print("Number is Odd")


# For not close immediately 
input("Press Enter to close program")


while True:
    # main program
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Invalid Input")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break