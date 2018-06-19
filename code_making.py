n = True
while n:
    print('''1. 0th and Last Index
2. Random Number Game
3. Book Uber
4. Prime Number
5. Distance between 1's in String''')
    a = input('Hello, which code do you want? \nEnter exit to Exit ')

    if a == '1':
        f = open("0index&lastIndex.py", "r")
        data = f.read()

        with open("/home/pulkit/Documents/0index&lastindex.py", "w") as file:
            file.write(data)
            print('Oth and Last Index created in Documents')
            file.close()

    elif a == '2':
        f = open("Random_Number_Game.py", "r")
        data = f.read()

        with open("/home/pulkit/Documents/Random_Number_Game.py", "w") as file:
            file.write(data)
            print('Random Number Game created in Documents')
            file.close()

    elif a == '3':
        f = open("uber_1to1.py", "r")
        data = f.read()

        with open("/home/pulkit/Documents/uber_1to1.py", "w") as file:
            file.write(data)
            print('Book Uber created in Documents')
            file.close()

    elif a == '4':
        f = open("prime_Number.py", "r")
        data = f.read()

        with open("/home/pulkit/Documents/prime_Number.py", "w") as file:
            file.write(data)
            print('Prime Number created in Documents')
            file.close()

    elif a == '5':
        f = open("Smallest_Largest_dis_1.py", "r")
        data = f.read()

        with open("/home/pulkit/Documents/Smallest_Largest_dis_1.py", "w") as file:
            file.write(data)
            print("Distance between 1's in String created in Documents")
            file.close()

    elif a == 'exit':
        n = False

    else:
        print('No valid input given!!')
        n = False