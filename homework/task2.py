class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, speaker, course, grade):
        if grade > 10:
            grade = 10      
        if isinstance(speaker, Lecturer) and course in self.courses_in_progress and course in speaker.courses_attached:
            if course in speaker.rating:
                speaker.rating[course] += [grade]
            else:
                speaker.rating[course] = [grade]
        else:
            return 'Ошибка'  
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.rating = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_homework(self, student, course, grade):
        if grade > 10:
            grade = 10
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


        
best_student = Student('Aleksei', 'Savin', 'Male')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_speaker = Lecturer('Best', 'Speaker')
cool_speaker.courses_attached += ['Python']

cool_mentor.rate_homework(best_student, 'Python', 9)
cool_mentor.rate_homework(best_student, 'C++', 2)
cool_mentor.rate_homework(best_student, 'Python', 6)

best_student.rate_lecture(cool_speaker, 'Python', 65)
best_student.rate_lecture(cool_speaker, 'Python', 8)
best_student.rate_lecture(cool_speaker, 'Java', 5) 

print(f'Оценки студента: {best_student.grades}')
print(f'Рейтинг лектора: {cool_speaker.rating}')