from random import randint

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, speaker, course, grade):
        '''
        Задание № 2. Определение функции выставления оценок лекторам
        '''
        if grade > 10:
            grade = 10      
        if (isinstance(speaker, Lecturer) 
            and course in self.courses_in_progress and course in speaker.courses_attached):
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
        '''
        Задание №3. Перегрузка метода __str__
        для класса Student
        '''
        average_grade = self.count_average_grade()
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {average_grade:.1f}\n'
            f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {', '.join(self.finished_courses)}'
        )       
    
    # Задание №3. Перегрузка логических операторов для сравнения студентов по средней оценке
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
        self.courses_attached = []
    
    # Задание №3. Перегрузка логических операторов для сравнения лекторов по среднему рейтингу
    def __eq__(self, other):
        return (self.count_average_rating() == other.count_average_rating() 
                if isinstance(self, Lecturer) else f'Экземпляр класса Reviever не имеет рейтинга')
    def __lt__(self, other):
        return (self.count_average_rating() < other.count_average_rating() 
                if isinstance(self, Lecturer) else f'Экземпляр класса Reviever не имеет рейтинга')
    def __le__(self, other):
        return (self.count_average_rating() <= other.count_average_rating() 
                if isinstance(self, Lecturer) else f'Экземпляр класса Reviever не имеет рейтинга')

class Lecturer(Mentor):
    '''
    Задание №1. Реализация дочернего/сыновьева класса Lecturer
    от Mentor
    '''    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}
        
    def count_average_rating(self):
        result_for_each_course = list(map(lambda x: sum(self.rating[x])/len(self.rating[x]), self.rating))
        return sum(result_for_each_course)/len(result_for_each_course)
    
    def __str__(self): 
        '''
        Задание №3. Перегрузка метода __str__
        для класса Lecturer
        '''
        average_rating = self.count_average_rating()
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {average_rating:.1f}'
        )
    
class Reviewer(Mentor):
    '''
    Задание №1. Реализация дочернего/сыновьева класса Reviever
    от Mentor
    '''
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_homework(self, student, course, grade):
        if grade > 10:
            grade = 10
        if (isinstance(student, Student) 
            and course in self.courses_attached and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        '''
        Задание №3. Перегрузка метода __str__
        для класса Reviever
        '''         
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}'
        )
    
def create_Student(name, surname, gender):
    '''
    Определение функции для одновременного создания экземпляра класса Student 
    и добавления его в список всех студентов
    '''
    name_of_copy = Student(name, surname, gender)
    all_students.append(name_of_copy)
    return name_of_copy

def count_course_rate(course):
    '''
    Задание 4. Определение функции подсчета средней оценки всех студентов по одному курсу
    '''
    students_on_course = [student for student in all_students if course in student.courses_in_progress]
    if len(students_on_course) > 0:
        all_rates = sum([student.grades[course] for student in students_on_course], [])
        return round(sum(all_rates)/len(all_rates), 1)
    else:
        return f'Введенные студенты на курсе {course} не учатся'

def count_course_rating(course, lectors):
    '''
    Задание 4. Функция подсчета средней оценки за лекции лекторов по одному курсу. 
    Новые функции не выдумывал
    '''
    lectors_on_course = [lector for lector in lectors if course in lector.courses_attached]
    if len(lectors_on_course) > 0:
        all_rates = sum([lector.rating[course] for lector in lectors], [])
        return round(sum(all_rates)/len(all_rates), 1)
    else:
        return f'Введенные лекторы на курсе {course} не преподают'

all_students = []
# Создание экземпляров Student
# best_student = Student('Aleksei', 'Savin', 'Male')
best_student = create_Student('Aleksei', 'Savin', 'Male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Создание телегабота']
# worst_student = Student('Ivanova', 'Ivana', 'Female')
worst_student = create_Student('Ivanova', 'Ivana', 'Female')
worst_student.courses_in_progress += ['Python', 'Git']
worst_student.finished_courses += ['Компуктерная грамотность']

# Создание экземпляров Reviewer
first_reviewer = Reviewer('First', 'Buddy')
first_reviewer.courses_attached += ['Python', 'Git']
second_reviewer = Reviewer('Second', 'Buddy')
second_reviewer.courses_attached += ['Python', 'Git']

# Создание экземпляров Lecturer
first_speaker = Lecturer('First', 'Speaker')
first_speaker.courses_attached += ['Python', 'Git']
second_speaker = Lecturer('Second', 'Speaker')
second_speaker.courses_attached += ['Python', 'Git']

# Выставление оценок best_student'у
first_reviewer.rate_homework(best_student, 'Python', randint(1, 15))
first_reviewer.rate_homework(best_student, 'Python', randint(1, 15))
second_reviewer.rate_homework(best_student, 'Python', randint(1, 15))
first_reviewer.rate_homework(best_student, 'Git', randint(1, 15))
second_reviewer.rate_homework(best_student, 'Git', randint(1, 15))
second_reviewer.rate_homework(best_student, 'Git', randint(1, 15))

# Выставление оценок worst_student'у
first_reviewer.rate_homework(worst_student, 'Python', randint(1, 15))
second_reviewer.rate_homework(worst_student, 'Python', randint(1, 15))
second_reviewer.rate_homework(worst_student, 'Python', randint(1, 15))
second_reviewer.rate_homework(worst_student, 'Git', randint(1, 15))
first_reviewer.rate_homework(worst_student, 'Git', randint(1, 15))
first_reviewer.rate_homework(worst_student, 'Git', randint(1, 15))

# Выставление оценок лекторам
best_student.rate_lecture(first_speaker, 'Git', randint(1, 15))
best_student.rate_lecture(first_speaker, 'Python', randint(1, 15))
worst_student.rate_lecture(first_speaker, 'Python', randint(1, 15))
best_student.rate_lecture(second_speaker, 'Python', randint(1, 15))
worst_student.rate_lecture(second_speaker, 'Git', randint(1, 15))
worst_student.rate_lecture(second_speaker, 'Git', randint(1, 15)) 

print('Проверка вывода перегруженного метода __str__')
print('Студенты:')
print(best_student)
print(worst_student)
print('\nПроверяющие:')
print(first_reviewer)
print(second_reviewer)
print('\nЛекторы:')
print(first_speaker)
print(second_speaker)

print('\nПроверка вывода перегруженных логических операторов')
print(round(best_student.count_average_grade(), 1),'>=', 
      round(worst_student.count_average_grade(), 1), best_student >= worst_student)
print(round(first_speaker.count_average_rating(), 1),'>', 
      round(second_speaker.count_average_rating(), 1), first_speaker > second_speaker)
print(first_reviewer <= second_reviewer)

print('\nПроверка функций подсчета средней оценки всех студентов в рамках одного курса')
print(f"Средняя оценка учащихся на курсе Python - {count_course_rate('Python')}")
print(f"Средняя оценка учащихся на курсе Git - {count_course_rate('Git')}")
print(f"Средняя оценка учащихся на курсе Java - {count_course_rate('Java')}")

print('\nПроверка функций подсчета среднего рейтинга введенных леторов в рамках одного курса')
print('Средний рейтинг лекторов на курсе Python -', 
      count_course_rating('Python', [first_speaker, second_speaker]))
print('Средний рейтинг лекторов на курсе Git -',
      count_course_rating('Git', [second_speaker]))
print('Средний рейтинг лекторов на курсе C++ -',
      count_course_rating('C++', [first_speaker]))