from typing import Dict

from classes.abc_store import AbstractStorage
from classes.class_courier import Courier
from classes.class_request import Request
from config.exeptions import BaseError
from config.func import get_shop, get_store, get_user_input_request, separator

# Доставить 15 сок из склад в магазин
# Доставить 3 печенька из склад в магазин


def main():
    print('Hello !\n')
    while True:

        for storage_name, storage in storages.items():
            print(f'В {storage_name} хранится:\n{storage.get_items()}', separator)

        get_request = get_user_input_request()
        if get_request in ['stop', 'стоп']:
            quit('Good bue !')

        try:
            request = Request(request=get_request, storages=storages)

        except BaseError as error:
            print(error.message)
            continue

        courier = Courier(request=request, storages=storages)
        try:
            courier.movie()

        except BaseError as error:
            print(error.message)
            courier.cancel()


if __name__ == '__main__':
    get_shop()
    get_store()
    storages: Dict[str, AbstractStorage] = {
        'склад': get_store(),
        'магазин': get_shop(),
    }
    main()
