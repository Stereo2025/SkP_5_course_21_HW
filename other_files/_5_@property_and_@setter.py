# Декораторы упрощающие работу с полями не нарушающие принципа инкапсуляции
# p - это property, m - метод
#


class Cat:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


cat = Cat('Barsik')
name = cat.name
print(name)


# cat.name() = 'New name'

# -------------------------------------------------------------------------------------------------------------- #
class Student:

    def __init__(self, name, course):
        self._name = name
        self._course = course

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value


student = Student('John', 2)

student_name = student.name
student_course = student.course

student.name = 'New name'
student.course = 1

print(student.name)
print(student.course)
