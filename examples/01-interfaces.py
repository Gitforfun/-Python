# define a simple class with operators (init, str, repr)
class Human:
    first_name: str
    last_name: str

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return "Human: " + self.__str__()


a = Human("John", "Doe")
b = Human("Artur", "Doe")
humans = [a, b]
# b = float(10.5)
# print(a)

print(humans)

# Data-class
