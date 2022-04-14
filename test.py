class Transport:
    ClassName = 'Transport'
    objCount = 0
    def __init__(self, color_, year_, type_):
        self.color = color_
        self.year = year_
        self.type = type_
        self.age = self.count_age()
        Transport.objCount += 1
    def stop(self):
        print('stop')
    def drive(self):
        print('drive')
    def count_age(self):
        return 2022 - self.year
    def info(self):
        print(self.color, self.age, self.year, self.type)
   

auto1 = Transport('red', 2009, 'truck')
auto2 = Transport('green', 2012, 'passenger car') 

auto1.drive()
auto1.stop()
auto2.info()
print(auto1.ClassName, auto2.ClassName)
print(Transport.objCount)

pass