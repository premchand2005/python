class Employee:
    company = "Google"
   
    def showDetails(self):
      print("This is an employee")
    
class programmer(Employee):
    language = "python"
    company = "youtube"
    def getLanguage(self):
       print(f"The language is {self.language}")
    
e = Employee()
e.showDetails()
p = programmer()
p.showDetails()      
print(p.company)      