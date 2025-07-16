class Employee:
    company = "Google"
    
def __init__(self, name, salary, subunit):
    self.name = name
    name.salary = salary 
    self.subunit = subunit
    print("Employee is created!")
    
def getDetails(self):
    print(f"the name of the employee is{self.name}")  
    print(f"the salary of the employee is{self.salary}")   
    print(f"the subunit of the employee is{self.subunit}")  
    
def getsalary(self,signature):
    print(f"salary for this employee workin in{self.company} is {self.salary}\n{signature}")    
    
@staticmethod
def greet():
    print("Good morning,sir/mamdam")    
    
@staticmethod
def time():
    print("The time is 9 AM in the morning")    
    
Harry = Employee('Harry',100,'youtube') 
Harry.getDetails()  