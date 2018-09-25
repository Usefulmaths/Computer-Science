import sys
sys.path.insert(0, '/Users/LiamEloie/Documents/Codes/Computer Science/Arrays and Strings')

from hash_table import HashTable
from time import time


class Fibonacci(object):
    def __init__(self):
        self.hash_table = HashTable(1000000)

    def iterate(self, n, use_hash=False):
        if n == 0:
            return 0

        if n == 1:
            return 1

        if use_hash:
            found = self.hash_table.find(str(n))

            if found:
                return found

            else:
                value = self.iterate(n - 1, use_hash) + self.iterate(n - 2, use_hash)
                self.hash_table.add(str(n), value)
                return value

        else:
            value = self.iterate(n - 1, use_hash) + self.iterate(n - 2, use_hash)
            return value


if __name__ == '__main__':
    fib = Fibonacci()

    # Calculate fibonacci without hash table.
    iterations = 10
    n = 950

    start = time()
    for i in range(iterations):
        a = fib.iterate(n, use_hash=True)

    print(a)
    end = time()

    print('Fibonacci for n = %d: %f' % (n, (end - start)/iterations))
