
class student :
    
    def __init__(self,Name,Age,Dob,Class):
        self.name = Name
        self.age = Age
        self.Dob = Dob
        self.CLass = Class
        print("This will always print when object created")
    
    def __del__(self):
        print("The object is deleted")

daksh = student("Daksh Singh",13,"6-6-2012",7)
aarav = student("Aarav Jain",12,"7-9-2012",7)


for i in range(1,100):
    print(i)
    i+=1

