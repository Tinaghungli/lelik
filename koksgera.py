class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.grades = []

    def add_grade(self, grade):
       
        self.grades.append(grade)

    def average_grade(self):
   
        if len(self.grades) == 0:
            return 0
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)


def print_student(student):
   
    print(f"Студент: {student.name}, группа {student.group}")
    print(f"Оценки: {student.grades}")
    print(f"Средний балл: {student.average_grade():.1f}")


def is_good_student(student):

    return student.average_grade() >= 4



st = Student("оля цымбал", "13/9")
st.add_grade(5)
st.add_grade(4)
st.add_grade(5)
print_student(st)
print("Отличник:", is_good_student(st))