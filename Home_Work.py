class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lectuer, course, grade):
        if isinstance(lectuer, Lecturer) and course in lectuer.courses_attached and course in self.courses_in_progress and 1 <= grade <= 10:
            if  course in lectuer.grades:
                lectuer.grades[course] += [grade]
            else:
                lectuer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached =[]
        
class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    
    def rate_hw(self, lectuer, student, course, grade):
        if isinstance(student, Student) and course in lectuer.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if  course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'Male')
best_student.add_courses('Git')
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]


cool_lectuer = Lecturer('Some', 'Buddy')
cool_lectuer.courses_attached += ['Python']


cool_reviewer = Reviewer('Ivan', 'Ivanov')
cool_reviewer.rate_hw(cool_lectuer, best_student, 'Python', 10)
cool_reviewer.rate_hw(cool_lectuer, best_student, 'Python', 10)
cool_reviewer.rate_hw(cool_lectuer, best_student, 'Python', 10)

print(best_student.grades)
print(cool_lectuer.grades)