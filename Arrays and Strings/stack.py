from linked_list import LinkedList


class Stack(object):
    def __init__(self):
        self.stack = LinkedList()

    def push(self, value):
        self.stack.insert(value, 0)

    def pop(self):
        self.stack.delete(0)

    def __str__(self):
        return self.stack.__str__()


if __name__ == '__main__':
    stack = Stack()

    stack.push('first in')
    print(stack)
    stack.push('second in')
    print(stack)
    stack.push('third in')
    print(stack)
    stack.pop()
    print(stack)
