from Delivery.Shop.shop import Shop
from Delivery.Store.store import Store
from Delivery.abstractClass.abstractnethod import Abstract


class Request(Abstract):
    def __init__(self, from_, to, amount, product):
        self.from_ = from_
        self.to = to
        self.amount = amount
        self.product = product

    def get_request(self):
        from_input = input('Откуда отправляем: ')
        to_input = input('Куда отправляем: ')
        product_import = input('Что отправляем: ')
        count_input = int(input('Количество: '))

# request = Request()
