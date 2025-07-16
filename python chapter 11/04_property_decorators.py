class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    
    @property
    def totalsalary(self):
        return self.salary + self.salarybonus
e = Employee()
print(e.totalsalary)     