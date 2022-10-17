# статический метод не принимает self. Статический метод это обычная публичная функция.
# статический метод не может менять ни self ни класс.

class PlayerRecords:

    @staticmethod
    def get_top_10():
        ...

    @staticmethod
    def get_top_100():
        ...

    @staticmethod
    def add_record(record):
        ...


# top_10 = PlayerRecords.get_top_10()


class Cat:

    def say(self):
        self.what_does_cat_say()

    @staticmethod
    def what_does_cat_say():
        print('Meow')


Cat.what_does_cat_say()

cat = Cat()
cat.what_does_cat_say()

cat = Cat()
cat.say()
