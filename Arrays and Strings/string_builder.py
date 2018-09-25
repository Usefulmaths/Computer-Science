from dynamic_array import DynamicArray
from time import time

class StringBuilder(object):
    def __init__(self):
        self.dynamic_array = DynamicArray()

    def append(self, word):
        self.dynamic_array.append(word)

    def to_string(self):
        string = ''.join(self.dynamic_array.array[:self.dynamic_array.array_size])

        return string

if __name__ == '__main__':
    words = ["My ", "name ", "is ", "Liam ", "and ",  "I ", "like ", "to ",  " program."]

    start = time()
    sentence = ""
    for word in words:
        sentence += word
    end = time()
    print(end - start)
    print(sentence)


    start = time()
    string_builder = StringBuilder()
    for word in words:
        string_builder.append(word)

    sentence = string_builder.to_string()
    end = time()

    print(end - start)
    print(sentence)

