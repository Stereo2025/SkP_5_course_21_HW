from classes.class_shop import Shop
from classes.class_store import Store


def get_user_input_request():
    request = input(f'Введите запрос в формате "Доставить 3 печенька из склад в магазин"\n'
                    f'Введите "стоп" или "stop" что бы завершить.\n-> : ').lower()
    return request


def get_store():
    store = Store(
        items={
            'молоко': 10,
            'сок': 15,
            'печенька': 5
        },
        capacity=100,
    )
    return store


def get_shop():
    shop = Shop(
        items={
            'горох': 10
        },
        capacity=20,
        max_items=5
    )
    return shop


separator = '\n' + '-' * 30 + '\n'
