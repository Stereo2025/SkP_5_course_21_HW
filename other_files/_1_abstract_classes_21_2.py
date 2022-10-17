from abc import ABC, abstractmethod, abstractproperty


class Resource(ABC):

    @abstractmethod
    def read(self):
        ...

    @abstractmethod
    def write(self):
        ...


class GoodFile(Resource):
    def __init__(self):
        pass

    def read(self):
        ...

    def write(self):
        ...


my_file = GoodFile()  # ОШИБОК НЕ БУДЕТ
my_file.read()


# class BadFIle(Resource):
#     def __init__(self):
#         pass
#
#     def get_data(self):
#         ...
#
#     def put_date(self):
#         ...
#
#
# my_file = BadFIle()  # TypeError: Can't instantiate abstract class BadFIle with abstract methods read, write
# my_file.read()  # TypeError: Can't instantiate abstract class BadFIle with abstract methods read, write


class BseCourse(ABC):

    @property
    @abstractmethod
    def title(self):
        ...

    @property
    @abstractmethod
    def description(self):
        ...

    @property
    @abstractmethod
    def credits(self):
        ...


class Course(BseCourse):

    def __init__(self, title, description, credits):
        self._title = title
        self._description = description
        self._credits = credits

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def credits(self):
        return self._credits


course = Course('Title', 'desc', 15)
