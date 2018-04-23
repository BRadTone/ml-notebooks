class Box:
    def __init__(self):
        pass

    def __len__(self):
        return 12

    def __repr__(self):
        return "I'm Box."

    def __add__(self, other):
        return 'Lets add'


c = Box()
b = Box()

print(c + b)
print(len(c))
print(repr(c))
