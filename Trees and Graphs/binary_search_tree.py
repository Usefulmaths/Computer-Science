class Node(object):
    '''
    A class representing a node in the binary search tree.
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    '''
    A class representing a binary search tree.
    '''
    def __init__(self):
        self.root = None

    def insertion(self, value, current_node=None):
        '''
        A recursive method for inserting a value (node)
        into the binary search tree.

        Arguments:
            value: the value the insert.
            current_node: the current node in the tree under consideration.
        '''
        node = Node(value)

        if self.root is None:
            self.root = node
            return

        if current_node is None:
            current_node = self.root

        current_value = current_node.value

        if value >= current_value:
            if not current_node.right:
                current_node.right = node
                return

            else:
                current_node = current_node.right
                self.insertion(value, current_node)

        else:
            if not current_node.left:
                current_node.left = node
                return

            else:
                current_node = current_node.left
                self.insertion(value, current_node)

    def search(self, value, current_node='root'):
        '''
        A recursive method for searching for a certain
        value in the binary search tree.

        Arguments:
            value: the value to search for in the binary search tree.
            current_node: the current_node under consideration.
        '''
        if current_node == 'root':
            current_node = self.root

        if current_node:
            if current_node.value == value:
                return True

            if value > current_node.value:
                current_node = current_node.right

            else:
                current_node = current_node.left

            return self.search(value, current_node)

        else:
            return False


if __name__ == '__main__':
    binary_search_tree = BinarySearchTree()

    number_list = [10, 5, 2, 5, 3, 9, 11, -1, 2, 17]

    for number in number_list:
        binary_search_tree.insertion(number)

    print(binary_search_tree.search(5))
    print(binary_search_tree.search(-1))
    print(binary_search_tree.search(0))
    print(binary_search_tree.search(-10))
    print(binary_search_tree.search(209))
    
