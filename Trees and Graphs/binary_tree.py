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

    def insert(self, value):
        '''
        Inserts a node into the tree using a breadth-first approach.

        Arguments:
            value: the value to be stored in the node
        '''

        if self.root is None:
            self.root = Node(value)

        else:
            queue = [self.root]

            while len(queue) != 0:
                node = queue[0]

                if node.left is None:
                    node.left = Node(value)
                    return value

                elif node.right is None:
                    node.right = Node(value)
                    return value

                del queue[0]
                queue.append(node.left)
                queue.append(node.right)

    def search(self, value, type='dfs'):
        '''
        Searches through the tree for a specific value using either 
        Depth-First Search (dfs) or Breadth-First Search. These implementations
        use a Stack/ Queue respectively.

        Arguments:
            value: the value of the node we are looking for.
            type: dfs or bfs

        Return:
            a boolean saying whether the value is in the tree or not.
        '''
        if type == 'dfs':
            stack = [self.root]

            while len(stack) != 0:
                node = stack[0]

                if node.value == value:
                    return True

                stack.pop(0)

                if node.right is not None:
                    stack.insert(0, node.right)

                if node.left is not None:
                    stack.insert(0, node.left)

            return False

        elif type == 'bfs':
            queue = [self.root]

            while len(queue) != 0:
                node = queue[0]

                if node.value == value:
                    return True

                queue.pop(0)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            return False


if __name__ == '__main__':
    binary_tree = BinaryTree()

    # Insert values breadth-first
    for i in range(100):
        binary_tree.insert(i)

    # In the tree
    print(binary_tree.search(54, type='dfs'))

    # In the tree
    print(binary_tree.search(54, type='bfs'))

    # Not in the tree
    print(binary_tree.search(-1, type='dfs'))

    # Not in the tree
    print(binary_tree.search(-1, type='bfs'))
