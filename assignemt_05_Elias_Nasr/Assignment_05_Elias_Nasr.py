class Course:
    def __init__(self, code, name, credit_hours, type):
        self.code = code
        self.name = name
        self.credit_hours = credit_hours
        self.type = type #core or elective

class Student(Course):
    def __init__(self, id, n, enrolled_course):
        self.id = id
        self.n = n
        self.enrolled_course = enrolled_course

class Enrollement_System:
    def __init__(self):
        self.students = []
        self.course_catalog = {} #keys are codes, values are course.name

    def addCourse(self, newcourse):
        # newcourse = Course()
        # newcourse.code = input("enter new course code: ")
        # newcourse.name = input("enter new course name")
        for i in course_catalog:
            if newcourse.code ==  i:
                return "this course already existed in catalog"
            else:
                course_catalog[newcourse.code] = newcourse.name
                return course_catalog
            
    #def enrollStudent():

    #def dropCourse():

    def listStudentCourses():
        courselist = []
        for course in course_catalog:
            if course == student.enrollStudent():
                courselist.append(course)
        print(f"list of course for {stydent.name}: {courselist}")
                
    def saveCourse():
        with open("filename", "w") as file:
            for course in course_catalog:
                if course.enrollStudent():
                    file.write(f"{course}\n")

    def loadCourse():
        with open("filename","r") as file:
            content = file.read
            print(f"course catalog: {content}\n")

            
system1 = Enrollement_System()
course_catalog = {}
def displayMenu():
    print("1.Add course \n2.Enroll student in course \n3.Drop course for student \n4.Liststudent courses \n5.Save course catalog: \n6.Load course catalog \n7.Exit")
    while (True):
        x = int(input("Enter your choice: "))
        if x == 1:
            specifiedcourse = Course(input("enter soecified course code: "), input("enter specified course name: "), input("enter credit hours: "), input("enter type: "))
            #specifiedcourse.code = input("enter new course code: ")
            #specifiedcourse.name = input("enter new course name: ")
            system1.addCourse(specifiedcourse)
            displayMenu()
        elif x == 2:
            system1.enrollStudent()
            displayMenu()
        elif x == 3:
            system1.dropCourse()
            displayMenu()
        elif x == 4:
            system1.listStudentCourses()
            displayMenu()
        elif x == 5:
            system1.saveCourse()
            displayMenu()
        elif x == 6:
            system1.loadCourse()
            displayMenu()
        elif x == 7:
            break
        else:
            print("invalid choice!")
            displayMenu()
        break

displayMenu()