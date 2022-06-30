from Delivery.Shop.shop import shop
from Delivery.Store.store import store


def main():
    while True:
        from_input = input('Откуда отправляем: ')
        if from_input == "склад":
            to_input = input('Куда отправляем: ')
            if to_input == "магазин":
                product_import = input('Что отправляем: ')
                if product_import in store.items.keys():
                    count_input = int(input('Количество: '))
                    if count_input > store.items[product_import]:
                        print('Количество в заказе превышает количества на складе')
                    elif count_input < store.items[product_import]:
                        print(f'Вы заказали {product_import} из {from_input} в кол-ве {count_input} штук в {to_input}')
                        store.remove(title=product_import, count=count_input)
                        print(
                            f'Отгружено со склада {product_import} - {count_input}штук, остаток - {store.get_unique_items_count(product_import)}штук')
                        shop.add(title=product_import, count=count_input)
                        print(f'В магазин приехали {product_import} - {count_input}штук')
                        print(
                            f'На складе осталось {store.get_free_space()}мест, в магазине {shop.get_free_space()}мест')
                else:
                    print('Такого товара нет')
            else:
                print('Нет такой точки приема')

        elif from_input == "магазин":
            to_input = input('Куда отправляем: ')
            if to_input == "склад":
                product_import = input('Что отправляем: ')
                if product_import in shop.items.keys():
                    count_input = int(input('Количество: '))
                    if count_input > shop.items[product_import]:
                        print('Количество в заказе превышает количества в магазине')
                    elif count_input < shop.items[product_import]:
                        print(f'Вы заказали {product_import} из {from_input} в кол-ве {count_input} штук в {to_input}')
                        shop.remove(title=product_import, count=count_input)
                        print(
                            f'Отгружено с магазина {product_import} - {count_input}штук, остаток - {shop.get_unique_items_count(product_import)}штук')
                        store.add(title=product_import, count=count_input)
                        print(f'На склад приехали {product_import} - {count_input}штук')
                        print(
                            f'На складе осталось {store.get_free_space()}мест, в магазине {shop.get_free_space()}мест')
                else:
                    print('Такого товара нет')
            else:
                print('Нет такой точки приема')

        else:
            print('Нет такой точки отправки')


main()
