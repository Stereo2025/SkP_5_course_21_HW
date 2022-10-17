# Инкапсуляция - это должны быть закрыты все те методы, которые не должны трогать другие части программы.
# Инкапсуляцию обеспечивают 2 основных приёма: 1) - разделение методов на публичные и приватные. 2) - скрытие полей
# за методами, которые называются get and set.

# Перед защищенными методами, которые называются protected ставиться один _. Напрямую не вызвать, те которые по
# соглашению мы не можем вызывать не из класса, но при этом они доступны, в том числе своим классам потомкам.

# У приватных методов два __ Приватный метод доступен только в области видимости класса. Они не доступны снаружи
# и не доступны классам потомкам.
#
#


class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def change_password(self, old_password, new_password):  # public
        self._is_password_correct(old_password)
        self._is_password_valid(new_password)
        self._was_password_used(new_password)

    def _is_password_correct(self, old_password):
        ...

    def _is_password_valid(self, new_password):
        ...

    def _was_password_used(self, new_password):
        ...


user = User('John', '123123')


class SomeClass:

    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def print(self):
        print(self._concat())

    def _concat(self):
        return f'{self.var1} {self.var2}'


object_1 = SomeClass(var1='Слава', var2='котикам')
object_1.print()
