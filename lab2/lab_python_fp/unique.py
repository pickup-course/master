#unique.py

from gen_random import gen_random

class Unique:
    def __init__(self, items, **kwargs):
        self.items = items
        self.values = set()
        self.ignore_case = kwargs.get('ignore_case', False)

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.items:
            if (not self.ignore_case and item not in self.values) or (self.ignore_case and str(item).lower() not in self.values):
                self.values.add(item if not self.ignore_case else str(item).lower())
                return item
        raise StopIteration

if __name__ == '__main__':   
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(list(Unique(data)))

    data = gen_random(10, 1, 3)
    print(list(Unique(data)))

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data)))
    print(list(Unique(data, ignore_case=True)))