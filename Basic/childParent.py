class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello from Parent {self.name}!"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the constructor of the Parent class
        self.age = age

    def greet(self):
        parent_greeting = super().greet()  # Call the greet method of the Parent class
        return f"{parent_greeting} I am {self.age} years old."

parent = Parent("Apoorva")
child = Child("Pooja", 10)

print(parent.greet())
print(child.greet())