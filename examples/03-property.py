# getter/setter examples, slow/fast, reload() property example
import random


class RandomList:
    _integers = None
    _floats = None

    @property
    def integers(self):
        if self._integers is None:
            self._integers = [random.randint(0, 100) for _ in range(10)]

        return self._integers

    @property
    def floats(self):
        if self._floats is None:
            self._floats = [random.random() for _ in range(10)]

        return self._floats

    def reset(self):
        self._integers = None
        self._floats = None


new_list = RandomList()

floats1 = new_list.floats
floats2 = new_list.floats

integers1 = new_list.integers
new_list.reset()
integers2 = new_list.integers
