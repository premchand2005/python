class Employee:
    company = "Visa"
    ecode = 120
    
class freelancer:
    company = "fiverr"
    level = 0 
    
    def upgradelevel(self):
        self.level = self.level +1 
        
class programmer(Employee,freelancer):
    name = "Premchand"
    
p = programmer()
p.upgradelevel()
print(p.level)               