class Student:
    
    def __init__(self, name, courses=None):
        self.name = name # string type
        self.courses = [] if courses is None else courses # list of strings
        self.num_courses = len(self.courses)
        
    def enroll_in_course(self, course_name):
        "Enrolls the student in a course."
        self.courses.append(course_name)
        self.num_courses += 1 # increment the number of courses
    
    def unenroll_in_course(self, course_name):
        "Unenrolls the student from a course."
        if course_name in self.courses:
            self.courses.remove(course_name)
            self.num_courses -= 1 # decrememt the number of courses
        else:
            print("Student was not enrolled in that course.")
