class Node(object):
    '''
    A class that represents a Node in a
    LinkedList.
    '''

    def __init__(self, value):
        self.value = value
        self.link = None

    def __del__(self):
        return None


class PriorityNode(Node):

    def __init__(self, value, priority):
        super().__init__(value)
        self.priority = priority


class LinkedList(object):
    '''
    A class that represents a Linked List.
    '''

    def __init__(self):
        self.head_value = None
        self.num_nodes = 0

    def append(self, value, priority=-1):
        '''
        Inserts a value at the head of the linked list.

        Arguments:
            value: the value to be added to the linked list.
        '''

        # Creates a Node object that stores a value.
        node = PriorityNode(value, priority)
        current = self.head_value

        # If the Linked List is empty, set Node to head.
        if current is None:
            self.head_value = node

        # If nodes already in Linked List, link the new node
        # to the head node and set the new node to the head node.
        else:
            while current.link:
                current = current.link

            current.link = node

        self.num_nodes += 1

    def delete(self, index):
        count = 0
        node = self.head_value

        if node is None:
            return

        if index == 0:
            self.head_value = node.link
            del node

        else:
            while count != index:
                previous_node = node
                node = node.link
                count += 1

            previous_node.link = node.link

        self.num_nodes -= 1

    def insert(self, value, index, priority=-1):
        current_node = self.head_value
        new_node = PriorityNode(value, priority)

        if index == 0:
            new_node.link = current_node
            self.head_value = new_node

        else:
            count = 0
            while count != index - 1:
                current_node = current_node.link
                count += 1

            next_node = current_node.link
            new_node.link = next_node
            current_node.link = new_node

        self.num_nodes += 1

    def index(self, ind):
        '''
        Traverses the Linked List to find the
        value at a specific index of the Linked
        List.

        Arguments:
            ind: the index of the Linked List

        Returns:
            value: the value corresponding to the
                   index in the Linked List.
        '''
        count = 0

        node = self.head_value

        while count != ind:
            node = node.link
            count += 1

        if node is None:
            return None

        value = node.value

        if node.priority == -1:
            return value

        else:
            return node

    def search(self, value):
        for i in range(self.num_nodes - 1):
            ind_value = self.index(i)

            if(ind_value == value):
                return True

        return False

    def __str__(self):
        string = ''

        node = self.head_value
        while node.link is not None:
            string += str(node.value) + " -> "
            node = node.link

        string += str(node.value)

        return string


if __name__ == '__main__':
    # Instantiate the Linked List.
    linked = LinkedList()

    linked.append('a stringg!')
    # Add some values to the Linked List.
    for i in range(12):
        linked.append(i)

    linked.append('a stringg!')
    linked.append('a stringg!')

    print(linked)
    linked.delete(1)
    print(linked)
    linked.delete(0)
    print(linked)
    linked.delete(4)
    print(linked)
    linked.insert('inserted node', 4)
    linked.insert('inserted node2', 0)
    print(linked)
