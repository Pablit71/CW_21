from HW_21.Delivery.abstractClass.abstractnethod import Abstract


class Shop(Abstract):
    def __init__(self):
        self.items = {
            "печеньки": 0,
            "собачки": 0,
            "коробки": 0
        }
        self.capacity_shop = 50 - sum(self.items.values())

    def add(self, title, count):
        self.items[title] += count
        self.capacity_shop -= count

    def remove(self, title, count):
        self.items[title] -= count
        self.capacity_shop += count

    def get_free_space(self):
        return self.capacity_shop

    def items(self):
        return self.items

    def get_unique_items_count(self, title):
        return self.items[title]


shop = Shop()
