#types of constructor
#default and parameterized
#default
class shinu:
    def __init__(self):
        self.name='Shivanshu'
        self.age=18
        print(self.name, self.age)


a1=shinu()
#parmeterized constructor
class shinu2:
    def __init__(self,name,age):
        self.name=name
        self.age=age

a=shinu2('Shivanshu',18)
print(a.name)
print(a.age)
