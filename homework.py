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

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) 
            and course in lecturer.courses_attached
            and course in self.courses_in_progress and 1 <= grade <= 10):
            if  course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_rating(self):
        all_grades = sum([grade for grade in self.grades.values()], [])
        if all_grades:
            return sum(all_grades)/len(all_grades)
        return 0
    
    def __completed_courses(self):
        if self.finished_courses:
            return ', '.join(self.finished_courses)
        return 'Нет завершенных курсов'
    
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка'
                f' за домашние задания: {self.average_rating():.1f}\n'
                f'Курсы в процессе изучения: '
                f'{", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {self.__completed_courses()}\n')


class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached =[]


class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        all_grades = sum([grade for grade in self.grades.values()], [])
        if all_grades:
            return sum(all_grades)/len(all_grades)
        return 0
    
    def __lt__(self, other):
        return self.average_rating() < other.average_rating()
    
    def __gt__(self, other):
        return self.average_rating() > other.average_rating()
    
    def __le__(self, other):
        return self.average_rating() <= other.average_rating()
    
    def __ge__(self, other):
        return self.average_rating() >= other.average_rating()
    
    def __eq__(self, other):
        return self.average_rating() == other.average_rating()
    
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка'
                f' за лекции: {self.average_rating():.1f}\n')


class Reviewer(Mentor):
    
    def rate_hw(self, lecturer, student, course, grade):
        if (isinstance(student, Student) 
            and course in lecturer.courses_attached
            and course in student.courses_in_progress and 1 <= grade <= 10):
            if  course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'
    

def average_homework(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades += student.grades[course]
    if all_grades:
        return (f'\nСредняя оценка за домашние задания по курсу {course}: '
                f'{sum(all_grades)/len(all_grades):.1f}')
    return f'\nНа курсе {course} у данных студентов нет оценок'


def average_lectures(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades += lecturer.grades[course]
    if all_grades:
        return (f'\nСредняя оценка за лекции по курсу {course}: '
                f'{sum(all_grades)/len(all_grades):.1f}')
    return f'\nПо курсу {course} у данных лекторов нет оценок'

best_student = Student('Ruoy', 'Eman', 'Male')
normal_student = Student('Ivan', 'Petrov', 'Male')

best_student.add_courses('Git')
best_student.courses_in_progress += ['Python', 'Java']
normal_student.courses_in_progress += ['C#']
best_student.grades['Git'] = [10, 10, 10, 10]

cool_lecturer = Lecturer('Some', 'Buddy')
normal_lecturer = Lecturer('Pavel', 'Kozlov')

cool_lecturer.courses_attached += ['Python', 'API']
normal_lecturer.courses_attached += ['C#', 'Java', 'Python']

cool_reviewer = Reviewer('Ivan', 'Ivanov')
normal_reviewer = Reviewer('Bogdan', 'Vavilov')

cool_reviewer.rate_hw(cool_lecturer, best_student, 'Python', 10)
cool_reviewer.rate_hw(cool_lecturer, best_student, 'Python', 10)
cool_reviewer.rate_hw(cool_lecturer, best_student, 'Java', 9)
cool_reviewer.rate_hw(normal_lecturer, best_student, 'Java', 9)
normal_reviewer.rate_hw(normal_lecturer, normal_student, 'C#', 8)
normal_reviewer.rate_hw(normal_lecturer, normal_student, 'C#', 10)
cool_reviewer.rate_hw(normal_lecturer, normal_student, 'C#', 9)

best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(normal_lecturer, 'Java', 9)
normal_student.rate_hw(normal_lecturer, 'C#', 10)
best_student.rate_hw(normal_lecturer, 'Python', 7)

print(cool_reviewer)
print(normal_reviewer)
print(cool_lecturer)
print(normal_lecturer)
print(best_student)
print(normal_student)
print(cool_lecturer > best_student)
print(cool_lecturer < best_student)
print(normal_lecturer >= normal_student)
print(cool_lecturer <= normal_student)
print(normal_lecturer == normal_student)
print(cool_lecturer != best_student)
print(average_homework([best_student, normal_student], 'C#'))
print(average_homework([best_student, normal_student], 'Python'))
print(average_homework([best_student, normal_student], 'C++'))
print(average_lectures([cool_lecturer, normal_lecturer], 'Python'))
print(average_lectures([cool_lecturer, normal_lecturer], 'C++'))
print(average_lectures([cool_lecturer, normal_lecturer], 'C#'))
print(average_lectures([cool_lecturer, normal_lecturer], 'Java'))