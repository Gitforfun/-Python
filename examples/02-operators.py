# +, -, <, >
# https://docs.python.org/3/library/operator.html


class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Operator +
        :param other:
        :return:
        """
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        """
        Operator -
        :param other:
        :return:
        """
        return Point(
            self.x - other.x,
            self.y - other.y
        )

    # def __truediv__(self, other):
    #     return Point(
    #         self.x / other.x,
    #         self.y / other.y
    #     )


A = Point(3, 5)
B = Point(10, -4)

C = A + B
print()
