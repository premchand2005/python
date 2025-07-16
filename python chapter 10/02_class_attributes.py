class Employee:
    company = "Google"

prem = Employee()
rajni = Employee()
print(prem.company)
print(rajni.company)
Employee.company = "YouTube" 
print(prem.company)
print(rajni.company)   
