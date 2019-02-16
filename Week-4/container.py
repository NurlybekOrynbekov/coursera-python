class Container:

    def __init__(self):
        self.dict = {}
    
    def __getitem__(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return 'Not Found'
    
    def __setitem__(self, key, value):
        self.dict[key] = value

    def __str__(self):
        return self.dict.__str__()


container = Container()

container['a'] = 15

print(container['a'])
print(container['b'])
print(container)