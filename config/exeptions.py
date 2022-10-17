class BaseError(Exception):
    message = 'Что то не так !'


class NotEnoughSpace(BaseError):
    message = 'Недостаточно места'


class NotEnoughProductError(BaseError):
    message = 'Недостаточно товара'


class TooManyDifferentProductError(BaseError):
    message = 'Слишком много разных товаров'


class InvalidRequestError(BaseError):
    message = 'Неправильный запрос'


class UnknownStorageError(BaseError):
    message = 'Неизвестный склад'
