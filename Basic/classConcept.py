class student:

    subject = "Python"
    #constructor
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}")


student1 = student("Apoorva", 20, 101)
student1.display_info()
print(f"Subject: {student.subject}")

class employee:
    __salary = 50000  # private variable

e=employee()
print(e._employee__salary)  # Accessing private variable using name mangling