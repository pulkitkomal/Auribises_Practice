class Projects:
    def __init__(self, pname):
        self.pname = pname

    def showProjects(self):
        print("Projects Submitted By student is with name {}".format(self.pname))


class Address:
    def __init__(self, adrsLine, city):
        self.adrsLine = adrsLine
        self.city = city

    def showAddress(self):
        print("Address of Customer is {} which is in {}".format(self.adrsLine, self.city))


class Student:

    def __init__(self, name, urn, phone, address, projects):
        self.name = name
        self.urn = urn
        self.phone = phone
        self.address = address
        self.projects = projects

    def showdetail(self):
        print("Student name is {} and rollno is {}".format(self.name, self.urn))

        for p in self.projects:
            p.showProjects()
        print("Address details of student is")
        self.address.showAddress()


class cse(Student):

    def __init__(self, tname, name, urn, phone, address, projects):
        super().__init__(name, urn, phone, address,projects)
        self.tname = tname

    def show(self):
        super().showdetail()
        print("Project has been submitted to {} for grading".format(self.tname))


a1 = Address("Country Homes", "Bengaluru")
name = input('What is your name? ')
n = int(input("enter no of projects"))
OrderList = []

for i in range(0, n):
    z = input("Enter Project details")
    OrderList.append(Projects(z))

tn = "Mr. Singh"
rn = 160066
s = cse(tn, name, rn, +9198989898, a1, OrderList)
s.show()