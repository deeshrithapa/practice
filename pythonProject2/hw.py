# 1.to check whether a person is eligible for voting or not.
v1 = int(input("enter your age:"))
if v1>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# 2. to check whether number entered by user is even or odd.
num = int(input("enter any number:"))
if num%2==0:
    print("even")
else:
    print("odd")

# 3. to check whether a number is divisible by 7 or not.
v1= int(input("enter any number:"))
if v1%7==0:
    print("it is divisible by 7")
else:
    print("it is not divisible by 7")

# 4. to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".
v1 = int(input("enter any number:"))
if v1%5==0:
    print("Hello")
else:
    print("Bye")

# 8. to accept a number from 1 to 7 and display the name of the day like 1 for Sunday, 7 for Saturday.
#  day = input("enter any value (1-7):")
day = int(day)
 if (day == 1):
     print("sun")
 if (day == 2):
     print("mon")
 if (day == 3):
     print("tue")
 if (day == 4):
     print("wed")
 if (day == 5):
     print("thur")
 if (day == 6):
     print("fri")
 if (day == 7):
     print("sat")
 if (day <= 0):
     print("others")
 if (day >= 8):
     print("others")

# 9. to accept a number from 1 to 12 and display name of the month and days in that
# month like 1 for Jan and number of days 31 and so on.
num = int(input("enter any number (1-12):"))
if (num == 1):
    print("january")
    print("number of days=31")
if (num==2):
    print("february")
    print("number of days=30")
if (num==3):
    print("march")
    print("number of days=31")
if (num==4):
    print("april")
    print("number of days=30")
if (num==5):
    print("may")
    print("number of days=31")
if (num==6):
    print("june")
    print("number of days=30")
if (num==7):
    print("july")
    print("number of days=31")
if (num==8):
    print("august")
    print("number of days=31")
if (num==9):
    print("september")
    print("number of days=30")
if (num==10):
    print("october")
    print("number of days=31")
if (num==11):
    print("november")
    print("number of days=30")
if (num==12):
    print("december")
    print("number of days=31")
if (num<1):
    print("out of range")
if (num>12):
    print("out of range")

# 11. to check whether a person is senior citizen or not.
num = int(input("enter your age:"))
if num>=60:
    print("senior citizen")
else:
    print("not senior citizen")

# 12.to find the largest number out of two numbers excepted from user.
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
if num1>num2:
    print("the largest number is:",num1)
else:
    print("the largest number is:",num2)

# 13. to find the largest number out of three numbers excepted from user.
v1= int(input("enter fisrt number:"))
v2= int(input("enter second number:"))
v3= int(input("enter third number:"))
if v1>v2 and v1>v3:
    print("the largest number is:",v1)
elif v2>v1 and v2>v3:
    print("the largest number is:",v2)
else:
    print("the largest number is:",v3)

# 14. to find the lowest number out of two numbers excepted from user.
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
if num1<num2:
     print("the lowest number is:",num1)
else:
     print("the lowest number is:",num2)

# 15. to find the lowest number out of three numbers excepted from user.
v1= int(input("enter fisrt number:"))
v2= int(input("enter second number:"))
v3= int(input("enter third number:"))
if v1<v2 and v1<v3:
    print("the lowest number is:",v1)
elif v2<v1 and v2<v3:
    print("the lowest number is:",v2)
else:
    print("the lowest number is:",v3)

# 16. to find the second largest number out of three numbers excepted from user.
v1= int(input("enter fisrt number:"))
v2= int(input("enter second number:"))
v3= int(input("enter third number:"))
if v1>v2 and v1<v3:
    print("the  second largest number is:",v1)
elif v2>v1 and v2<v3:
    print("the  second largest number is:",v2)
else:
    print("the second largest number is:",v3)

# 17. to find the second lowest number out of three numbers excepted from user.
v1= int(input("enter fisrt number:"))
v2= int(input("enter second number:"))
v3= int(input("enter third number:"))
if v1>v2 and v1<v3:
    print("the  second lowest number is:",v1)
elif v2>v1 and v2<v3:
    print("the  second lowest is:",v2)
else:
    print("the  second lowest number is:",v3)

# 18.program to check whether a number is even or odd.
num1 = int(2)
if num1%2==0:
    print("even")
else:
    print("odd")

# 19. to check whether a number (accepted from user) is divisible by 2 and 3 both.
v1 = int(input("enter any number:"))
if v1%2 == 0 and v1%3 == 0:
    print("yes it is divisible")
else:
    print("no it is not divisible")

#to check whether the year is leap or not
num4 = int(input("enter a year:"))
if num4%4 == 0 and num4%100 == 0 or num4%400==0:
    print("leap year")
else:
    print("not a leap year")

#to display the last digit of number
num2 = int(input("enter any number:"))
print(num2%10)



