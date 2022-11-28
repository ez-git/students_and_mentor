

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print('Ошибка: студент не изучает курс учителя')
        else:
            print('Ошибка: объект не является экземляром класса')

    def average_rating_by_grades(self):
        if isinstance(self, Student):
            all_grades = self.grades.values()
            sum_of_all_grades = 0
            count = 0
            for elem in all_grades:
                sum_of_all_grades += sum(elem)
                count += len(elem)
            number_of_ratings = len(all_grades)
            if number_of_ratings == 0:
                return 0
            else:
                return round(sum_of_all_grades / count, 1)
        else:
            return 0

    def __str__(self):
        if isinstance(self, Student):
            return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                   f'Средняя оценка за лекции: {self.average_rating_by_grades()}\n' \
                   f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                   f'Завершенные курсы: {", ".join(self.finished_courses)}'
        else:
            return 'Ошибка: объект не является экземляром класса'

    def __lt__(self, other):
        if isinstance(self, Student):
            return int(self.average_rating_by_grades()) < int(other.average_rating_by_grades())
        else:
            return 'Ошибка: объект не является экземляром класса'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating_by_grades(self):
        if isinstance(self, Lecturer):
            all_grades = self.grades.values()
            sum_of_all_grades = 0
            count = 0
            for elem in all_grades:
                sum_of_all_grades += sum(elem)
                count += len(elem)
            number_of_ratings = len(all_grades)
            if number_of_ratings == 0:
                return 0
            else:
                return round(sum_of_all_grades / count, 1)
        else:
            return 0

    def __str__(self):
        if isinstance(self, Lecturer):
            return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                   f'Средняя оценка за лекции: {self.average_rating_by_grades()}'
        else:
            return 'Ошибка: объект не является экземляром класса'

    def __lt__(self, other):
        if isinstance(self, Lecturer):
            return int(self.average_rating_by_grades()) < int(other.average_rating_by_grades())
        else:
            return 'Ошибка: объект не является экземляром класса'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student):
            if course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                print('Ошибка: преподаватель не прикреплен к курсу ученика')
        else:
            print('Ошибка: объект не является экземляром класса')

    def __str__(self):
        if isinstance(self, Reviewer):
            return f'Имя: {self.name}\nФамилия: {self.surname}'
        else:
            return 'Ошибка: объект не является экземляром класса'


def hw_average(students: list, course: str):
    for student in students:
        all_grades = student.grades.values()
        sum_of_all_grades = 0
        count = 0
        for elem in all_grades:
            sum_of_all_grades += sum(elem)
            count += len(elem)
        number_of_ratings = len(all_grades)
        if number_of_ratings == 0:
            return 0
        else:
            return round(sum_of_all_grades / count, 1)


def lecturers_average(lecturers: list, course: str):
    for lecturer in lecturers:
        all_grades = lecturer.grades.values()
        sum_of_all_grades = 0
        count = 0
        for elem in all_grades:
            sum_of_all_grades += sum(elem)
            count += len(elem)
        number_of_ratings = len(all_grades)
        if number_of_ratings == 0:
            return 0
        else:
            return round(sum_of_all_grades / count, 1)


student1 = Student('sName1', 'sSurname1', 'm')
student2 = Student('sName2', 'sSurname2', 'm')
student3 = Student('sName3', 'sSurname3', 'f')

student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Java']
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Java']

lecturer1 = Lecturer('lName1', 'lSurname1')
lecturer2 = Lecturer('lName2', 'lSurname2')
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Java']

reviewer1 = Reviewer('rName1', 'lSurname1')
reviewer2 = Reviewer('rName2', 'rSurname2')

reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Java']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 5)
reviewer2.rate_hw(student1, 'Python', 10)

reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 8)

student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 9)

print(student1)
print(student2)
print(lecturer1)
print(reviewer1)

print(student1 < lecturer1)
print(student1 > lecturer1)

