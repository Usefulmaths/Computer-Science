from linked_list import LinkedList


class Queue(object):

    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value, priority=-1):
        self.queue.append(value, priority)

    def dequeue(self):
        self.queue.delete(0)

    def __str__(self):
        return self.queue.__str__()


class MaxPriorityQueue(Queue):

    def __init__(self):
        super().__init__()

    def enqueue(self, value, priority=-1):
        self.queue.append(value, priority)

    def dequeue(self):
        max_priority, max_priority_value, max_index = self.peak()
        self.queue.delete(max_index)

    def peak(self):
        max_priority = -1E10
        max_priority_value = None

        num_nodes = self.queue.num_nodes

        for node_index in range(num_nodes):
            node = self.queue.index(node_index)
            priority = node.priority

            if priority > max_priority:
                max_priority = priority
                max_priority_value = node.value
                max_index = node_index

        return max_priority, max_priority_value, max_index


class MinPriorityQueue(Queue):

    def __init__(self):
        super().__init__()

    def enqueue(self, value, priority=-1):
        self.queue.append(value, priority)

    def dequeue(self):
        min_priority, min_priority_value, min_index = self.peak()
        self.queue.delete(min_index)

    def peak(self):
        min_priority = 1E10
        min_priority_value = None

        num_nodes = self.queue.num_nodes

        for node_index in range(num_nodes):
            node = self.queue.index(node_index)
            priority = node.priority

            if priority < min_priority:
                min_priority = priority
                min_priority_value = node.value
                min_index = node_index

        return min_priority, min_priority_value, min_index


if __name__ == '__main__':
    print('### Standard Queue ###')
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print('Enqueue: ')
    print(queue)
    print('Dequeue: ')
    queue.dequeue()
    print(queue)

    print('\n### Min Priority Queue ###')
    queue = MinPriorityQueue()
    queue.enqueue(1, priority=1)
    queue.enqueue(2, priority=10)
    queue.enqueue(3, priority=0.5)
    print('Enqueue: ')
    print(queue)
    print('Dequeue: ')
    queue.dequeue()
    print(queue)

    print('\n### Max Priority Queue ###')
    queue = MaxPriorityQueue()
    queue.enqueue(1, priority=1)
    queue.enqueue(2, priority=10)
    queue.enqueue(3, priority=0.5)
    print('Enqueue: ')
    print(queue)
    print('Dequeue: ')
    queue.dequeue()
    print(queue)
