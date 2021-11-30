from model.student import Student


class DataRepository:
    students = [
        Student("Carlos", "Castillo", 22),
        Student("Carlos", "Lopez", 21),
        Student("Jhandry", "Lopez", 24),
        Student("Gerson", "Santos", 21)
    ]

    def get_students(self):
        return self.students

    def search_student_by_pos(self, pos):
        pos -= 1
        if 0 <= pos < len(self.students):
            return self.students[pos]
        return None

    def search_student_by_name(self, name):
        return filter(lambda student: student.get_name() == name, self.students)

    def search_student_by_lastname(self, lastname):
        return filter(lambda student: student.get_lastname() == lastname, self.students)

    def search_student_by_age(self, age):
        return filter(lambda student: student.get_age() == age, self.students)

    def add_student(self, data_student):
        self.students.append(
            Student(data_student['name'], data_student['lastname'], data_student['lastname'])
        )

    def update_student(self, pos, data_student):
        self.students[pos - 1] = Student(data_student['name'], data_student['lastname'], data_student['lastname'])

    def delete_student(self, pos):
        self.students.pop(pos - 1)