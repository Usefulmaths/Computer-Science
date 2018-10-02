from linked_list import LinkedList


class Queue(object):

    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value, priority=-1):
        self.queue.append(value, priority)

    def dequeue(self):
        self.queue.delete(0)

    def priority_max_peak(self):
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

    def priority_min_peak(self):
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

    def max_priority_dequeue(self):
        max_priority, max_priority_value, max_index = self.priority_max_peak()
        self.queue.delete(max_index)

    def min_priority_dequeue(self):
        min_priority, min_priority_value, min_index = self.priority_min_peak()
        self.queue.delete(min_index)

    def peak(self):
        first_element = self.queue.index(0).value
        return first_element

    def __str__(self):
        return self.queue.__str__()

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1, priority=1)
    queue.enqueue(2, priority=10)
    queue.enqueue(3, priority=5)
    print(queue)

    queue.min_priority_dequeue()
    print(queue)

    print(queue.peak())
