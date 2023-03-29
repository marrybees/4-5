# class People:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#     def get_gmail(self):
#         print(self.get_gemil)


# class Student(People):
    def __init__(self, firstname, lastname, courses):
        super().__init__(firstname, lastname)
        self.courses = courses

    def get_gmail(self):
        print(f"{self.firstname}.{self.lastname}.@1edu.ge")


class Leqturer(People):
    def xelfaxi(self, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_gmail(self):
        print(f"{self.firstname}.{self.lastname}.@1edu.ge")


f1 = Leqturer('firstname', 'lastname')
f1.get_gmail()
f2 = Student('fiestname', 'lastname','saganebi')
f2.get_gmail()
homework2
class Librarytem:
    def __init__(self,title,subject,status):
        self.title = title
        self.subject = subject
        self.status = status
class Book(Librarytem):
    def __init__(self,title,subject,status,authors,ISBN):
        super().__init__(title,subject,status)
        self.authors = authors
        self.ISBN = ISBN
class Magazine(Librarytem):
    def __init__(self,jurnalname,volume,status):
        super().__init__(status)
        self.jurnalname = jurnalname
        self.volume = volume
class CD:
    def __init__(self,title,status):
        super().__init__(title,status)

# #homrwork3
class Person:
    def __init__(self,firstname,lastname,age):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
    def __str__(self):
        return f"gvaria {self.lastname},saxelia {self.firstname},asakia{self.age}"
class Employee(Person):
    def __int__(self,profession,monthly_salary,working_hurs):
        self.profession = profession
        self.monthly_salary = monthly_salary
        self.working_hours = working_hurs
    def hourly_salary(self):
class Doctor(Person):
    def __init__(self,firstname,lastname,age,profession,monthly_salary,working_hurs):
            super().__init__(firstname,lastname,age,monthly_salary,working_hurs,profession)
    def perform_operation(self):



