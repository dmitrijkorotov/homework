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
        if (isinstance(lectuer, Lecturer) and course in lectuer.courses_attached
            and course in self.courses_in_progress and 1 <= grade <= 10):
            if  course in lectuer.grades:
                lectuer.grades[course] += [grade]
            else:
                lectuer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_rating(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
        return sum(all_grades)/len(all_grades)
    
    def __completed_courses(self):
        if self.finished_courses:
            return ', '.join(self.finished_courses)
        return 'Нет завершенных курсов'
    
    def __str__(self):
        return (f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка'
                f' за домашние задания: {self.average_rating():.1f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {self.__completed_courses()}')


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
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
        return sum(all_grades)/len(all_grades)
    
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
        return (f'\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка'
                f' за лекции: {self.average_rating():.1f}')


class Reviewer(Mentor):
    
    def rate_hw(self, lectuer, student, course, grade):
        if (isinstance(student, Student) and course in lectuer.courses_attached
            and course in student.courses_in_progress and 1 <= grade <= 10):
            if  course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'\nИмя: {self.name}\nФамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'Male')
best_student.add_courses('Git')
best_student.add_courses('Java')
best_student.courses_in_progress += ['Python', 'API']
best_student.grades['Git'] = [10, 10, 10, 10, 10]



cool_lectuer = Lecturer('Some', 'Buddy')
cool_lectuer.courses_attached += ['Python', 'API']


cool_reviewer = Reviewer('Ivan', 'Ivanov')
cool_reviewer.rate_hw(cool_lectuer, best_student, 'Python', 10)
cool_reviewer.rate_hw(cool_lectuer, best_student, 'Python', 10)
cool_reviewer.rate_hw(cool_lectuer, best_student, 'Python', 10)
best_student.rate_hw(cool_lectuer, 'Python', 10)
best_student.rate_hw(cool_lectuer, 'Python', 10)
best_student.rate_hw(cool_lectuer, 'API', 10)


print(best_student <= cool_lectuer)
print(cool_reviewer)
print(cool_lectuer)
print(best_student)
print(best_student.grades)
print(cool_lectuer.grades)