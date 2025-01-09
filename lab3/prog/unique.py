#unique.py

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