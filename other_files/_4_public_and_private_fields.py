# Get - метод с помощью которого можно получать значение класса, объекта и т.д
# Set - метод с помощью которых мы можем задавать новые значения.
#
#
#

class Player:

    def __init__(self):
        self._hits = 0

    def add_hit(self):
        self._hits += 1


class User:

    def __init__(self, name):
        self._name = name

    def set_name(self, new_name):  # setter
        self._name = new_name

    def get_name(self):  # getter
        return self._name


user_1 = User('John')
user_1.set_name('Artur')
print(user_1.get_name())
