# extend default classes (int - currency)
class Currency(float):
    sign = ' RUB'

    def __str__(self):
        return super(Currency, self).__str__() + self.sign


salary = Currency(200)
print(salary)
