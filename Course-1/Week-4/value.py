class Value:

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        self.amount = int(value - obj.commission * value)