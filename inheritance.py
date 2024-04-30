class Car:  # Base class
    number_of_sales = 0

    @classmethod
    def sales_number(cls):
        return f"number of sales: {cls.number_of_sales}"

    def __init__(self, car_type, serial_number):
        self.car_type = car_type
        self.serial_number = serial_number

        Car.number_of_sales += 1


class Audi(Car):  # Derived class
    number_of_sales = 0
    def __init__(self, car_type, serial_number, price):
        super().__init__(car_type, serial_number)
        self.price = price
        Audi.number_of_sales +=1
        


# Base class usage
car1 = Car("toyota", 1234)
car2 = Car("hunda", 3214)
car3 = Car("isuzu", 1432)

print(car1.car_type)
print(car1.serial_number)

print(car2.car_type)
print(car2.serial_number)

print(car3.car_type)
print(car3.serial_number)

print(f"number of sales: {Car.sales_number()}")

print("#"*50)

# Derived class usage
audi1 = Audi("audi1", 1234, 120000)
audi2 = Audi("audi2",1424,130000)
audi3 = Audi("audi3",1543,140000)
audi4 = Audi("audi4",1793,150000)
print(audi1.car_type)
print(audi1.serial_number)
print(audi1.price)

print(audi2.car_type)
print(audi2.serial_number)
print(audi2.price)

print(audi3.car_type)
print(audi3.serial_number)
print(audi3.price)

print(audi4.car_type)
print(audi4.serial_number)
print(audi4.price)

print(f"number of sales:{Audi.sales_number()}")
