class DynamicArray(object):
    '''
    A class representing a Dynamic Array,
    doubles in size when current capacity
    is full.
    '''
    def __init__(self):
        self.array = [None]

        self.array_size = 0
        self.max_size = 1

    def append(self, value):
        '''
        Appends a value to the array. If the
        array is full, the capacity will double.

        Arguments:
            value: the value to be added to the array.
        '''

        if self.array_size == self.max_size:
            self.max_size = self.max_size * 2
            self.new_array = [None] * self.max_size

            for index in range(self.array_size):
                self.new_array[index] = self.array[index]

            self.array = self.new_array

        self.array[self.array_size] = value
        self.array_size += 1

    def index(self, ind):
        '''
        Finds a value at a given index
        in the array.

        Arguments:
            ind: the index to search.

        Returns:
            value: the corresponding value.
        '''

        value = self.array[ind]

        return value

    def __str__(self):
        return str(self.array)

if __name__ == '__main__':
    # Instantiates a dynamic array of size 1.
    dynamic_array = DynamicArray()

    # Append 100 integers to the dynamics array.
    for i in range(100):
        dynamic_array.append(i)

    # Returns the value at index 93 (93)
    print(dynamic_array.index(93))
