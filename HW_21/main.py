from Delivery.Shop.shop import shop
from Delivery.Store.store import store
from HW_21.Delivery.Request.request import Request
from HW_21.Delivery.utils import balance

while True:
    print(f'На складе есть:\n{balance(store.items)}\n{"*" * 50}\nВ магазине:\n{balance(shop.items)}\n{"*" * 50}\n')
    user_input = input("Запрос: ").lower()
    request = Request(user_input)
    if request.from_ == "склад":
        if request.to == "магазин":
            if request.product in store.items.keys():
                if request.amount > store.items[request.product]:
                    print(
                        f'Количество в заказе превышает количества на складе, не хватает - {request.amount - store.get_unique_items_count(request.product)} ')
                elif request.amount < store.items[request.product]:
                    print(
                        f'Вы заказали {request.product} из {request.from_} в кол-ве {request.amount} штук в {request.to}')
                    if shop.get_free_space() < request.amount:
                        print("В магазине нет места")
                    else:
                        store.remove(title=request.product, count=request.amount)
                        print(
                            f'Отгружено со склада {request.product} - {request.amount}штук, остаток - {store.get_unique_items_count(request.product)}штук')
                        shop.add(title=request.product, count=request.amount)
                        print(f'В магазин приехали {request.product} - {request.amount}штук')
            else:
                print('Такого товара нет')
                break
        else:
            print('Нет такой точки приема')
            break

    elif request.from_ == "магазин":
        if request.to == "склад":
            if request.product in shop.items.keys():
                if request.amount > shop.items[request.product]:
                    print(
                        f'Количество в заказе превышает количества в магазине, не хватает - {request.amount - shop.get_unique_items_count(request.product)}')
                elif request.amount < shop.items[request.product]:
                    print(
                        f'Вы заказали {request.product} из {request.from_} в кол-ве {request.amount} штук в {request.to}')
                    if store.get_free_space() < request.amount:
                        print("На складе нет места")

                    else:
                        shop.remove(title=request.product, count=request.amount)
                        print(
                            f'Отгружено с магазина {request.product} - {request.amount}штук, остаток - {shop.get_unique_items_count(request.product)}штук')
                        store.add(title=request.product, count=request.amount)
                        print(f'На склад приехали {request.product} - {request.amount}штук')
            else:
                print('Такого товара нет')

        else:
            print('Нет такой точки приема')

    else:
        print('Нет такой точки отправки')
