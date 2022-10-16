# to check even or odd
num = int(input("enter any number:"))
if num%2==0:
    print("even")
else:
    print("odd")

#to check positive, negative or zero
num1 = int(input("enter any number:"))
if num1>0:
    print("positive")
elif num1<0:
    print("negative")
else:
    print("it is neither positive nor nagative")

#to display the last digit of number
num2 = int(input("enter any number:"))
print(num2%10)

#to check if the last digit of the number is divisible by 7
num3= int(input("enter any number:"))
num4= (num3%10)
if num4%7==0:
    print("it is divisible by 7")
else:
    print("it is not divisible by 7 ")

#to check whether the year is leap or not
num4 = int(input("enter a year:"))
if (num4%4 == 0 and num4%100 == 0) or (num4%400==0):
    print("leap year")
else:
    print("not a leap year")
a
