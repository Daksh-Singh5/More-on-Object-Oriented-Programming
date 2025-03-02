class employee:
    def __init__(self,empId,Name,salary,Post):
        self.empId = empId
        self.name = Name
        self.salary = salary
        self.Post = Post
    
    def printobject(self):
            print("emp ID: ",self.empId)
            print("Name: ",self.name)
            print("Salary: ",self.salary)
            print("Post: ",self.Post)
    def changeName(self,changedName):
            self.name=changedName
    def __del__(self):
        print("The employee",self.name,"is deleted")


daksh = employee(1,"Daksh Singh",662012,"manager")
daksh.printobject()
changenameinto = input("which name do you want to change into: ")
daksh.changeName(changenameinto)
daksh.printobject()



        