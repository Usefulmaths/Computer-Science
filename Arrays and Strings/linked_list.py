
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


class LinkedList(object):
    '''
    A class that represents a Linked List.
    '''
    def __init__(self):
        self.head_value = None
        self.num_nodes = 0

    def append(self, value):
        '''
        Inserts a value at the head of the linked list.

        Arguments:
            value: the value to be added to the linked list.
        '''

        # Creates a Node object that stores a value.
        node = Node(value)
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

        if index == 0:
            self.head_value = node.link
            del node

        else:
            while count != index:
                previous_node = node
                node = node.link
                count += 1

            previous_node.link = node.link

    def insert(self, value, index):
        current_node = self.head_value
        new_node = Node(value)

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

        value = node.value

        return value

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
