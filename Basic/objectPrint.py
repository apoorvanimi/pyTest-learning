class obj:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
       # return "value of name is: " + self.name + " and value of age is: " + str(self.age)
      #  return "value of name is %s and value of age is %s" %(self.name,self.age)

  #  def __repr__(self):
   #     return f"obj(name={self.name}, age={self.age})"

o=obj("Apoorva", 20)
print(o)  # Calls __str__ method#
#print(repr(o))  # Calls __repr__ method