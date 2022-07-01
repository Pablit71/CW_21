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

req_start = Request._start()
# req_to = request.to
# req_product = request.product
# req_amount = request.amount
