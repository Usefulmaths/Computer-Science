class BubbleSort(object):
    '''
    A class that represents the bubble sort algorithm
    '''
    def __init__(self, array):
        self.array = array
        self.array_size = len(array)

    def sort(self):
        '''
        Call the bubble sort algorithm
        '''

        # Iterate through every element in the array.
        for i in range(self.array_size):
            index = 0

            # Iterate through every element up until
            # the elements that have already been sorted.
            while index < self.array_size - 1 - i:

                # Retrieve the element under consideration.
                element = self.array[index]

                # Retrieve the next element
                next_element = self.array[index + 1]

                # If the next element is smaller than
                # the current element, switch their
                # indices.
                if next_element <= element:
                    self.array[index] = next_element
                    self.array[index + 1] = element

                # Iterate through the indices.
                index += 1

        sorted_array = self.array

        return sorted_array


if __name__ == '__main__':
    array = [15, 2, 1, 17, 18, 4, -1]
    bubble_sort = BubbleSort(array)
    bubble_sort.sort()
