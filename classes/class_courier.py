from typing import Dict

from classes.abc_store import AbstractStorage
from classes.class_request import Request


class Courier:

    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        self.departure = storages[self.__request.departure]
        self.destination = storages[self.__request.destination]

    def movie(self):

        self.departure.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забирает {self.__request.amount} {self.__request.product} из {self.__request.departure}')

        print(f'Курьер везет {self.__request.amount} {self.__request.product} '
              f'со {self.__request.departure} в {self.__request.destination}')

        self.destination.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}')

    def cancel(self):
        if self.__request.amount and self.__request.product \
                not in [self.__request.departure, self.__request.destination]:
            self.departure.add(name=self.__request.product, amount=self.__request.amount)
            print(f'Доставка отменена...\n'
                  f'Курьер вернул {self.__request.amount} {self.__request.product} '
                  f'обратно в {self.__request.destination}')
