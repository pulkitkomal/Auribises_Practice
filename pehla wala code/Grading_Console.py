import statistics as m
students = {'pulkit': [70, 70, 70], 'sourav': [90, 90, 90], 'himanshu': [80, 80, 80]}

def addgrades():
    w = input('Enter Name: ')
    e = input('Enter Grade: ')
    h = int(e)
    students[w].append(h)
    print(students)

def removestudent():
    t = input('Enter Name: ')
    del students[t]
    print(students)

def avstudnts():
    for s in students:
        grades = students[s]
        avg = m.mean(grades)
        print(s, 'has an average of ', avg)
def addstudent():
    u = input('Name of student: ')
    o = input('Enter marks of one subject: ')
    j = str(u)
    k = int(o)
    v = [k]
    students[j] = v
    print(students)

def main():
    print(''' Welcome to Grading Console
        #1. To Add Student.
        #2. To Remove student.
        #3. To Add Grades.
        #4. To Find Total Average.
        #4. Exit.
            ''')
    q = input("What would you like to do today: ")
    j = int(q)
    if j == 1:
        addstudent()
    if j == 2:
        removestudent()
    if j == 3:
        addgrades()
    if j == 4:
        avstudnts()
    if j == 5:
        exit()

user = input('Enter Username: ')
passs = input('Enter Password: ')
if user == 'abc' and passs == '123':
    while True:
        main()
else:
        print('Bye Bye')