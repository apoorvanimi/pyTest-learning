def print_values():
    print("This is a function to print values")
    total=100
    num=int(input("Enter your number: "))
    if num>0:
        print("The number is positive")
        total=total+num
        print("The total is:",total)
    elif num<0:
        print("The number is negative")
        total=total+num
        print("The total is:",total)
    else:
        print("The number is zero")
        print("The total is:",total)

#call function
print_values()

def facorial(num):
    if num==0:
        return 1
    else:
        return num*facorial(num-1)

print("Factorial of 5 is:",facorial(5))

print("username is %s and password is %s" %("apoorva","1234"))
def getmarks(*args):
    for i in args:
        print(i)

getmarks(10,20,30,40,50)

def getmarks1(**kwargs):
    for key,value in kwargs.items():
      print("%s == %s" %(key,value))

getmarks1(English=10,Maths=20,Science=30,Social=40)

#lambda function
square=lambda x:x*x
print("Square of 5 is:",square(5))