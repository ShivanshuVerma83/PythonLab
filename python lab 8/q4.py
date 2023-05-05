class temperature:
    temp=0
    def __init__(self,temp):
        self.temp=temp
    def convertfahrenheit(self):
        ans=float((9*self.temp)/5 +32)
        return ans
    def convertcelsius(self):
        ans = float((self.temp-32)*5/9)
        return ans



input_temp = float(input("Input temperature in celsius: "))
temp1 = temperature(input_temp)
print(temp1.convertfahrenheit())

input_temp = float(input("Input temperature in fahrenheit: "))
temp1 = temperature(input_temp)
print(temp1.convertcelsius())