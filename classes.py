class Customer:

    number_of_customers = 0
    
    @classmethod #has at least one parameter
    def customer_count(cls): #count customers using class method
        return f"we have {cls.number_of_customers} customers"
    
    @staticmethod #has no parameters
    def static_method():
        return "hello dear customer"

    def __init__(self,fname,lname,gender,price):
        self.fname = fname
        self.lname = lname
        self.price = price
        self.gender = gender
        Customer.number_of_customers += 1

    def welcome_message(self):
        if self.gender == "male":
            return f"Hello Mr {self.fname} {self.lname}"  
        elif self.gender == "female":
            return f"Hello mrs {self.fname} {self.lname}"

    def get_discount(self):
        self.discount =  self.price - (self.price // 10)
        return f"your price after making discount : {self.discount}"
    
    def del_customer(self): #count customers using instance method
        Customer.number_of_customers -= 1
        return f"customer {self.fname} has been deleted"


# class usage
print( f"\n{Customer.static_method()}\n") #using static method

print(f"number of users : {Customer.number_of_customers}")
Customer1 = Customer("ali","mohamed","male".lower(),2500)
Customer2 = Customer("salwa","ahmed","female".lower(),2000)
Customer3 = Customer("ahmed","mohmoud","male".lower(),1050)
Customer4 = Customer("mona","maher","female".lower(),1200)
print(Customer1.welcome_message())
print(Customer1.get_discount())
print(Customer2.welcome_message())
print(Customer2.get_discount())
print(Customer3.welcome_message())
print(Customer3.get_discount())
print(Customer4.welcome_message())
print(Customer4.get_discount())
print(f"number of users : {Customer.number_of_customers}")
print("#"*50)
print(Customer2.del_customer())
print(f"number of users : {Customer.number_of_customers}") #number of users using instance method
print("#" * 50)
print(Customer.customer_count())  # number of users using class method
