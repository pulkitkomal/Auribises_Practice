class Uber:
    def __init__(self, name, cab):
        self.name = name
        self.cab = cab

    def showDetails(self):
        print('Welcome ', self.name)
        self.cab.show()



class cab:
    def __init__(self, pickup, destination, typeCab):
        self.pickup = pickup
        self.destination = destination
        self.typecab = typeCab

    def show(self):
        print('You have booked an Uber {} from {} to {}'.format(self.typecab, self.pickup, self.destination))


u1 = input('Your Name? ')
c1 = input('From where should I pick you up? ')
c2 = input('Where to? ')
c3 = input('What kind of vehicle would you prefer(Go, X, Moto) ? ')
c = cab(c1, c2, c3)
m1 = Uber(u1, c)
m1.showDetails()

