from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.curr = 0

    def __next__(self):
        try:
            result = self.data[self.curr]
        except IndexError:
            raise StopIteration
        self.curr += 1
        return result
