class Employee:
    company = "Google"
    salary = 100
prem = Employee()
rajni = Employee()
print(prem.company)
print(rajni.company)
prem.salary = 300
rajni.salary =200
Employee.company = "YouTube" 
print(prem.company)
print(rajni.company)   
print(prem.salary)
print(rajni.salary)