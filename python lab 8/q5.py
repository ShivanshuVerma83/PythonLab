
#Brand,cpu,ram,processor and  price
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = None  # lap is the obj of a inner class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:  # inner class
        def __init__(self, brand, cpu, ram, processor, price):
            self.brand = brand
            self.cpu = cpu
            self.ram=ram
            self.processor=processor
            self.price=price

        def show(self):
            print(self.brand, self.cpu, self.ram, self.processor, self.price)


s1 = Student('Ram', 21)
s1 = Student('am', 21)
s1 = Student('m', 21)
s1 = Student('abc', 21)
s1 = Student('def', 21)
lap1 = s1.Laptop('Dell', 'i3','8GB', '43Ghz',72000)
lap2 = s1.Laptop('hp', 'i3','8GB', '43Ghz',72000)
lap3 = s1.Laptop('asus', 'i3','8GB', '43Ghz',72000)
lap4 = s1.Laptop('hp', 'i3','8GB', '43Ghz',72000)
lap5 = s1.Laptop('Dell', 'i3','8GB', '43Ghz',72000)
lap1.show()
lap2.show()
lap3.show()
lap4.show()
lap5.show()