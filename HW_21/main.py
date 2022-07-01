from Delivery.Shop.shop import shop
from Delivery.Store.store import store
from HW_21.Delivery.utils import balance


class Request:
    def __init__(self, start):
        self.start = self._start()
        self.to = self._to()
        self.product = self._product()
        self.amount = self._amount()

    @staticmethod
    def _start():
        start = input('Откуда отправляем: ')
        return start

    @staticmethod
    def _to():
        to = input('Куда отправляем: ')
        return to

    @staticmethod
    def _product():
        product = input('Что отправляем: ')
        return product

    @staticmethod
    def _amount():
        amount = int(input('Количество: '))
        return amount


while True:
    print(f'На складе есть:\n{balance(store.items)}\nВ магазине:\n{balance(shop.items)}')
    req_start = Request._start()
    if req_start == "склад":
        req_to = Request._to()
        if req_to == "магазин":
            req_product = Request._product()
            if req_product in store.items.keys():
                req_amount = Request._amount()
                if req_amount > store.items[req_product]:
                    print(f'Количество в заказе превышает количества на складе, не хватает - {req_amount - store.get_unique_items_count(req_product)} ')
                elif req_amount < store.items[req_product]:
                    print(
                        f'Вы заказали {req_product} из {req_start} в кол-ве {req_amount} штук в {req_to}')
                    if shop.get_free_space() < req_amount:
                        print("В магазине нет места")
                    else:
                        store.remove(title=req_product, count=req_amount)
                        print(
                            f'Отгружено со склада {req_product} - {req_amount}штук, остаток - {store.get_unique_items_count(req_product)}штук')
                        shop.add(title=req_product, count=req_amount)
                        print(f'В магазин приехали {req_product} - {req_amount}штук')
                        print(
                            f'На складе:\n {balance(store.items)}\nВ магазине:\n{balance(shop.items)}')
                        continue_input = input("Будем еще что-то заказывать? ")
                        if continue_input == "нет":
                            break
                        elif continue_input == "да":
                            continue
            else:
                print('Такого товара нет')
                break
        else:
            print('Нет такой точки приема')
            break

    elif req_start == "магазин":
        req_to = Request._to()
        if req_to == "склад":
            req_product = Request._product()
            if req_product in shop.items.keys():
                req_amount = Request._amount()
                if req_amount > shop.items[req_product]:
                    print(f'Количество в заказе превышает количества в магазине, не хватает - {req_amount - shop.get_unique_items_count(req_product)}')
                elif req_amount < shop.items[req_product]:
                    print(
                        f'Вы заказали {req_product} из {req_start} в кол-ве {req_amount} штук в {req_to}')
                    if store.get_free_space() < req_amount:
                        print("На складе нет места")

                    else:
                        shop.remove(title=req_product, count=req_amount)
                        print(
                            f'Отгружено с магазина {req_product} - {req_amount}штук, остаток - {shop.get_unique_items_count(req_product)}штук')
                        store.add(title=req_product, count=req_amount)
                        print(f'На склад приехали {req_product} - {req_amount}штук')
                        print(
                            f'На складе:\n {balance(store.items)}\nВ магазине:\n{balance(shop.items)}')
                        continue_input = input("Будем еще что-то заказывать? ")
                        if continue_input == "нет":
                            break
                        elif continue_input == "да":
                            continue
            else:
                print('Такого товара нет')

        else:
            print('Нет такой точки приема')

    else:
        print('Нет такой точки отправки')
