# Write a program to accept percentage from the user and display the grade according to the following criteria:

#          Marks                                    Grade
#          > 90                                         A
#          > 80 and <= 90                       B
#          >= 60 and <= 80                       C
#          below 60                                  D

print("Enter your marks for grade - gradding system ")

marks = int(input("Enter Your Marks : "))

if(marks>90):
    grade = "A"
elif(marks>80 and marks<=90):
    grade = "B"
elif(marks>=60 and marks<=80):
    grade = "C"
elif(marks<60):
    grade = "D"
else:
    print("You are Failed ")
