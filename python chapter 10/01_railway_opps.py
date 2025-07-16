class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"name is {self .name}")
        print(f"train is {self.train}")
        
premApplication = RailwayForm()
premApplication.name = "Prem"
premApplication.train = "Rajdhani Express"
premApplication.printData()        