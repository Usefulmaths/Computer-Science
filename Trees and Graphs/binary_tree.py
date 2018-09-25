class Node(object):
    '''
    A class representing a node in a binary tree
    '''

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    '''
    A class representing a binary tree data structure.
    '''

    def __init__(self):
        self.root = None

    def insert(self, value, current_node=None):
        '''
        A recursive method for the insertion of a node in a binary tree. Uses
        a Depth-First approach in finding an empty child.

        Arguments:
            node: the node that needs inserting
            current_node: current_node being access for empty spaces.
        '''
        node = Node(value)
        if self.root is None:
            self.root = node
            return

        if current_node is None:
            current_node = self.root

        if current_node.left is None:
            current_node.left = node
            return True

        elif current_node.right is None:
            current_node.right = node
            return True

        else:
            return self.insert(value, current_node.left) or self.insert(value, current_node.right)

    def search(self, value, parent_node='root'):
        '''
        A recursive search method using pre-order Depth-First search to find
        a certain node in the binary tree.

        Arguments:
            value: the value to search for.
            parent_node: the current node being searched for the value.
        '''
        if parent_node is 'root':
            parent_node = self.root

        # Pre-order
        if parent_node:
            if parent_node.value == value:
                return True

            else:
                return self.search(value, parent_node.left) or self.search(value, parent_node.right)

        else:
            return False


if __name__ == '__main__':
    binary_tree = BinaryTree()

    for i in range(10):
        binary_tree.insert(i)

    print(binary_tree.search(0))
    print(binary_tree.search(4))
    print(binary_tree.search(7))
    print(binary_tree.search(9))
    print(binary_tree.search(10))
    print(binary_tree.search(-1))
