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
        
    def count_average_grade(self):
        results_for_each_course = list(map(lambda x: sum(self.grades[x])/len(self.grades[x]), self.grades))
        return sum(results_for_each_course)/len(results_for_each_course)
    
    def __str__(self):
        average_grade = self.count_average_grade()
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {average_grade:.1f}\n'
            f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {', '.join(self.finished_courses)}'
        )       
    
    def __eq__(self, other):
        return self.count_average_grade() == other.count_average_grade()
    def __lt__(self, other):
        return self.count_average_grade() < other.count_average_grade()
    def __le__(self, other):
        return self.count_average_grade() <= other.count_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        if isinstance(self, Reviewer):
            return (
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}'
            )
        else:
            average_rating = self.count_average_rating()
            return (
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {average_rating:.1f}'
            )
    def __eq__(self, other):
        return self.count_average_grade() == other.count_average_grade() if isinstance(self, Lecturer) else f'Экземпляр класса не имеет рейтинга'
    def __lt__(self, other):
        return self.count_average_grade() < other.count_average_grade() if isinstance(self, Lecturer) else f'Экземпляр класса не имеет рейтинга'
    def __le__(self, other):
        return self.count_average_grade() <= other.count_average_grade() if isinstance(self, Lecturer) else f'Экземпляр класса не имеет рейтинга'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.rating = {}
        
    def count_average_rating(self):
        result_for_each_course = list(map(lambda x: sum(self.rating[x])/len(self.rating[x]), self.rating))
        return sum(result_for_each_course)/len(result_for_each_course)
        

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
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Создание телегабота']
worst_student = Student('Ivanov', 'Ivan', 'Female')
worst_student.courses_in_progress += ['Python', 'Git']

first_reviewer = Reviewer('First', 'Buddy')
first_reviewer.courses_attached += ['Python', 'Git']
second_reviewer = Reviewer('Second', 'Buddy')
second_reviewer.courses_attached += ['Python', 'Git']

first_speaker = Lecturer('Second', 'Speaker')
first_speaker.courses_attached += ['Python', 'Git']
second_speaker = Lecturer('Second', 'Speaker')
second_speaker.courses_attached += ['Python', 'Git']

first_reviewer.rate_homework(best_student, 'Python', 9)
first_reviewer.rate_homework(best_student, 'Python', 8)
first_reviewer.rate_homework(best_student, 'Python', 90)
first_reviewer.rate_homework(best_student, 'Git', 6)
first_reviewer.rate_homework(best_student, 'Git', 9)

first_reviewer.rate_homework(worst_student, 'Python', 2)
first_reviewer.rate_homework(worst_student, 'Python', 3)
first_reviewer.rate_homework(worst_student, 'Python', 1)
first_reviewer.rate_homework(worst_student, 'Git', 2)
first_reviewer.rate_homework(worst_student, 'Git', 3)

best_student.rate_lecture(first_speaker, 'Python', 10)
best_student.rate_lecture(first_speaker, 'Python', 10)
best_student.rate_lecture(first_speaker, 'Java', 1) 

# print(f'Оценки студента: {best_student.grades}')
# print(f'Рейтинг лектора: {cool_speaker.rating}')

print(best_student.count_average_grade())
print(worst_student.count_average_grade())
print(first_reviewer > second_reviewer)