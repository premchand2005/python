class Employee:
    company = "camel"
    salary = 100
    location = "khorimahua"
    
    # def changesalary(self,sal):
    #     self.__class__.salary = sal
        
    @classmethod
    def changesalary(cls,sal):
            cls.salary = sal
        
e = Employee()
print(e.salary)
e.changesalary(2003)
print(e.salary)
print(Employee.salary)             