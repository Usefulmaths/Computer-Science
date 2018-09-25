from linked_list import LinkedList


class DataPair(object):
    '''
    A class that stores a key-value pair.
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    '''
    A class that represent a Hash Table.
    '''
    def __init__(self, array_size):
        self.linked_lists = [None] * array_size
        self.array_size = array_size

    def hash_function(self, key):
        '''
        A hash function that is used to map a key
        to an index that is used to assign the
        key-value pair a specific Linked List.

        Arguments:
            key: the key for the key-value pair.
        '''
        return sum(map(lambda c: ord(c), key))

    def add(self, key, value):
        '''
        Adds a key-value pair to the hash table.

        Arguments:
            key: the key of the key-value pair.
            value: the value of the key-value pair.
        '''
        data_pair = DataPair(key, value)

        hash = self.hash_function(key)

        index = hash % self.array_size

        if self.linked_lists[index] is None:
            self.linked_lists[index] = LinkedList()

        self.linked_lists[index].append(data_pair)

    def find(self, key):
        '''
        Finds the key-value pair in the Hash Table
        given the key.

        Arguments:
            key: the key of the key-value pair.

        Returns:
            value: the value of the key-value pair.
        '''
        hash = self.hash_function(key)
        index = hash % self.array_size

        linked_list = self.linked_lists[index]

        if linked_list is None:
            return None

        not_found = True
        count = 0
        while not_found:
            if count == linked_list.num_nodes:
                return None

            else:

                data_pair = linked_list.index(count)

                if data_pair.key == key:
                    not_found = True
                    value = data_pair.value

                    return value

                count += 1


if __name__ == '__main__':
    hash_table = HashTable(array_size=1000)

    hash_table.add('Liam', 23)
    hash_table.add('Bill', 57)
    hash_table.add('Martin', 15)

    print(hash_table.find('Liam'))
