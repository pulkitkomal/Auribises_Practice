import mysql.connector
class Student:

    def __init__(self, roll, name, age, email, address):
        self.roll = roll
        self.name = name
        self.age = age
        self.email = email
        self.address = address

    def showStudent(self):
        print("Roll Number {} belongs to {}".format(self.roll,self.name))

    def getStudentDetails(self):
        data = "{},{},{},{},{}\n".format(self.roll, self.name, self.age, self.email, self.address)
        return data

s1 = Student(1,"John",20,"john@example.com","Redwood Shores")
s2 = Student(2,"Jennie",30,"jennie@example.com","Country Homes")

s1.showStudent()
s2.showStudent()

con = mysql.connector.connect(user="root",password="",host="localhost",database="test")
print("Is Connection Established:",con.is_connected())
print(type(con))
cursor = con.cursor()
print(type(cursor))


sql2 = "insert into test('{}',{},'{}','{}')".format(s1.name,s1.age,s1.email,s1.address)


cursor.execute(sql2)

con.commit()
print("Student Saved !!")