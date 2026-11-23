#list
names=["rahul","pooja","priya"]
for name in names:
    print(name)

#Tuple
marks=(90,80,70,60,50,90,80,70,60,50)
for mark in marks:
    print(mark)
    print("The total marks are:",sum(marks))
    print("The average marks are:",sum(marks)/len(marks))
    print("The maximum marks are:",max(marks))
    print("The minimum marks are:",min(marks))
    print("The sorted marks are:",sorted(marks))
    print("The reversed marks are:",list(reversed(marks)))
    print("The length of marks are:",len(marks))
    print("The count of marks are:",marks.count(90))
    print("The index of marks are:",marks.index(90))
    print("The type of marks are:",type(marks))
    print("The id of marks are:",id(marks))
    print("The hash of marks are:",hash(marks))
    print(marks[1:5])
 
#Set
lan={"python","java","c++","c#","javascript"}
lan.add("ruby")
lan.remove("c++")
print(lan)

#set functions
s1=set("pythonn")
print(s1)

#union
p1={1,2,3,4,5}
p2={4,5,6,7,8}
p3={6,7,8}
print("Union of p1 and p2 is:",p1.union(p2))
print("Intersection of p1 and p2 is:",p1.intersection(p2))
print("Difference of p1 and p2 is:",p1.difference(p2))
print("Symmetric difference of p1 and p2 is:",p1.symmetric_difference(p2))
print("Is p1 a subset of p2?",p3.issubset(p2))
