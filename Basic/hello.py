print ("Hello, World!")
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

# loop
i=1
while(i<10):
    print(i)
    i=i*2

#For loop
names=["apoorva","pooja","priya"]
for index in range(len(names)):
    print(names[index])

for i in range(1,5):
    for j in range(i):
        print(i,end=" ")
    print()
    