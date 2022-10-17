# Полиморфизм - это свойство системы использовать объекты с одинаковым интерфейсом, без информации о типе
# или структуре внутреннем устройстве этого объекта.
import json


class TextFile:

    def read(self, file):
        with open(file) as f:
            return f.readlines()

    def write(self, file, lines):
        ...


class JSONFile:

    def read(self, file):
        with open(file) as f:
            return json.load(f)

    def write(self, file, lines):
        ...


file_processor_txt = TextFile()
data_txt = file_processor_txt.read('data.txt')
print(data_txt)

file_processor_json = JSONFile()
data = file_processor_json.read('data.json')
print(data)
