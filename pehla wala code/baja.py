class projects:
    def __init__(self, project):
        self.project = project

    def show1(self):
        print('Projects are',self.project)


class Address:

    def __init__(self, address):
        self.address = address

    def show2(self):
        print('Address is', self.address)


class GNDEC:
    def __init__(self, name, urn, projects, address):
        self.name = name
        self.urn = urn
        self.projects = projects
        self.address = address

    def show(self):
        print('-----------------------')
        print('Name is', self.name)
        print('Roll No.', self.urn)
        self.address.show2()
        for p in self.projects:
            p.show1()


class cseStudent(GNDEC):
    pass


stdName = input('Name? ')
rlNo = int(input("Roll No.? "))
ad = input('Address? ')
pro = []
i1 = int(input('Enter No. of Projects? '))
for i in range(0, i1):
        i2 = input('Project {} Name? '.format(i+1))
        pro.append(projects(i2))
a1 = Address(ad)
c = cseStudent(stdName, rlNo, pro, a1)
c.show()