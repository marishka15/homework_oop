class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def av_grade_for_homework(self):
        sum_grade = 0
        len_grade = 0
        for course in self.grades.values():
            sum_grade += sum(course)
            len_grade += len(course)
        av_grade_for_homework = round(sum_grade / len_grade, 2)
        return av_grade_for_homework

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating_for_course = round(sum_rating / len_rating, 2)
        return average_rating_for_course

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_grade_for_homework()}\nКурсы в процессе обучения: {"".join(self.courses_in_progress)}\nЗавершенные курсы: {"".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Преподователей и студентов между собой не сравниваем")
            return
        return self.av_grade_for_homework() < other.av_grade_for_homework()
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_grade_for_course(self):
        sum_grade = 0
        len_grade = 0
        for course in self.grades.values():
            sum_grade += sum(course)
            len_grade += len(course)
        av_grade_for_course = round(sum_grade / len_grade, 2)
        return av_grade_for_course

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        av_rating_for_course = round(sum_rating / len_rating, 2)
        return av_rating_for_course

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.av_grade_for_course()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Преподователей и студентов между собой не сравниваем")
            return
        return self.av_grade_for_course() < other.av_grade_for_course()
class Reviewer(Mentor):

    def __int__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

#Студенты
best_student_1 = Student('Иван', 'Иванов', 'муж')
best_student_1.courses_in_progress += ['Python']
best_student_1.finished_courses += ["Введение в програмирование"]

best_student_2 = Student('Антон', 'Петров', 'муж' )
best_student_2.courses_in_progress += ['Python']
best_student_2.finished_courses += ["Введение в програмирование"]

#Проверяющие
cool_reviewer_1 = Reviewer('Кристина', 'Игоревна')
cool_reviewer_1.courses_attached += ['Python']

cool_reviewer_2 = Reviewer('Олег', 'Иванов')
cool_reviewer_2.courses_attached += ['Python']

#Лекторы
lecturer_1 = Lecturer('Андрей', 'Андреев')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Марина', 'Маринова')
lecturer_2.courses_attached += ['Python']

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
cool_reviewer_1.rate_hw(best_student_1, 'Python', 9)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 8)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 7)

cool_reviewer_2.rate_hw(best_student_2, 'Python', 10)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 10)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 5)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
best_student_1.rate_lecturer(lecturer_1, 'Python', 10)
best_student_1.rate_lecturer(lecturer_1, 'Python', 9)
best_student_1.rate_lecturer(lecturer_1, 'Python', 9)

best_student_2.rate_lecturer(lecturer_2, 'Python', 8)
best_student_2.rate_lecturer(lecturer_2, 'Python', 8)
best_student_2.rate_lecturer(lecturer_2, 'Python', 8)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
student_list = [best_student_1, best_student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [cool_reviewer_1, cool_reviewer_2]

def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating

print(best_student_1)
print(best_student_2)
print(lecturer_1)
print(lecturer_2)
print(average_rating_for_course('Python', student_list))
print(average_rating_for_course('Python', lecturer_list))
