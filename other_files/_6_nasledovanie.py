# super() -  спец функция, основное применение - реализация доступа к родительским классам внутри дочерних.
# Будет работать до тех пор, пока наследник не ПЕРЕОПРЕДЕЛИЛ эти методы

class Book:

    def __init__(self, name, pages, content, author):
        self.name = name
        self.pages = pages
        self.content = content
        self.author = author


class EBook(Book):

    def __init__(self, name, pages, content, author, links):
        super().__init__(name, pages, content, author)
        self.links = links


book_1 = Book("Книга Python", 300, 'Уроки', 'Я')
book_2 = EBook("Книга Python", 300, 'Уроки', 'Я', ['http://library.io/book/006.pdf'])


# -------------------------------------------------------------------------------------------------------------- #

class StoreItem:

    def calculate(self, count):
        return self._calculate_tax(count) + (count * 100)

    def _calculate_tax(self, count):
        return 0


class StoreItemInternational(StoreItem):

    def _calculate_tax(self, count):
        return count * 0.5


item = StoreItemInternational()
item.calculate(10)


# -------------------------------------------------------------------------------------------------------------- #
class PrintedProduct:

    def __init__(self, name, pages, content):
        self.name = name
        self.pages = pages
        self.content = content


class Boook(PrintedProduct):

    def __init__(self, name, pages, content, author):
        super().__init__(name, pages, content)
        self.author = author


class Magazine(PrintedProduct):

    def __init__(self, name, pages, content):
        super().__init__(name, pages, content)
