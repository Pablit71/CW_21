from Delivery.abstractClass.abstractnethod import Abstract


class Store(Abstract):
    def __init__(self):
        self.items = {
            "печеньки": 20,
            "собачки": 20,
            "коробки": 20
        }
        self.capacity = 100 - sum(self.items.values())

    def add(self, title, count):
        self.items[title] += count
        self.capacity -= count

    def remove(self, title, count):
        self.items[title] -= count
        self.capacity += count

    def get_free_space(self):
        return self.capacity

    def items(self):
        return self.items

    def get_unique_items_count(self, title):
        return self.items[title]


store = Store()
