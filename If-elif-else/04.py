# Write a program to display "Hello" if a number entered by user is a multiple of five , 
# otherwise print "Bye".

print("Program displayed - 'Hello' or 'Bye' If user Entered Number multiple of 5")

num = int(input("Enter the Number : "))
if(num%5==0):
    print("Hello")
else:
    print("Bye")

# For not close immediately 
input("Press Enter to close program")
