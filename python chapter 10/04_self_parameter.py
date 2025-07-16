class Employee:
    company = "Google"
    def getsalary(self):
        print("salary is 70k")
        
prem = Employee()
prem.getsalary()        




class Employee:
    company = "Google"
    def getsalary(self):
        print(f"salary is : {self.salary }")
        
prem = Employee()
prem.salary =   700000
prem.getsalary()        