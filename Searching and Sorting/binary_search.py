class BinarySearch(object):
    def __init__(self, array):
        self.array = array

    def search(self, value):
        partition = self.array

        min_point = 0
        max_point = len(partition)

        mid_point = int((min_point + max_point) / 2)

        while True:
            if partition[mid_point] == value:
                return True

            if mid_point == min_point or mid_point == max_point:
                return False

            if partition[mid_point] < value:
                min_point = mid_point

            else:
                max_point = mid_point

            mid_point = int((min_point + max_point) / 2)


if __name__ == '__main__':
    array = [1, 2, 23, 93, 102, 105]
    binary_search = BinarySearch(array)
    present = binary_search.search(105)
    print(present)
