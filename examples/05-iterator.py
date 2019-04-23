# class for iterable object
# random numbers list
import random


class MyIterator:
    _numbers: list

    def __init__(self, numbers_count):
        self._numbers = [random.randint(1, 100) for _ in range(numbers_count)]

    def __iter__(self):
        # for ... in ...
        return self

    def __next__(self):
        if len(self._numbers) > 0:
            return self._numbers.pop()
        else:
            raise StopIteration


my_iterator = MyIterator(30)

for x in my_iterator:
    print(x)
