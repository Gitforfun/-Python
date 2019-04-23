# static class example, static fields (constants), methods (helpers), global list
import math


class MathHelperSome:
    pi = 3.14  # constants

    @staticmethod
    def factorial(number: int):
        # MathHelper.pi
        return math.factorial(number)

    @classmethod
    def simple_test(cls):
        # cls.pi
        print(cls)


# expr = 10 * MathHelper.pi
# print(expr)

# a = MathHelper()
# a.pi = 10

# result = MathHelper.factorial(5)


class User:
    STATUS_DISABLED = 0
    STATUS_ACTIVE = 1
    STATUS_BANNED = 2

    login: str = 'admin'
    password: str = '123123'
    status: int = 0

    def activate(self):
        self.status = self.STATUS_ACTIVE

    def ban(self):
        self.status = self.STATUS_BANNED

    @property
    def is_active(self):
        return self.status == self.STATUS_ACTIVE


user_list = [
    User(), User(), User()
]

active_users = filter(lambda x: x.status == User.STATUS_ACTIVE, user_list)
active_users = filter(lambda x: x.is_active, user_list)
