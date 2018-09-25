from linked_list import LinkedList


class Queue(object):
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        self.queue.delete(0)

    def peak(self):
        first_element = self.queue.index(0)
        return first_element

    def __str__(self):
        return self.queue.__str__()

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)

    queue.dequeue()
    print(queue)

    print(queue.peak())
