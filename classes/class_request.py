from typing import Dict

from classes.abc_store import AbstractStorage
from config.exeptions import InvalidRequestError, UnknownStorageError


class Request:

    def __init__(self, request: str, storages: Dict[str, AbstractStorage]):

        get_request = request.strip().lower().split(' ')
        if len(get_request) != 7:
            raise InvalidRequestError

        self.amount = int(get_request[1])
        self.product = get_request[2]
        self.departure = get_request[4]
        self.destination = get_request[6]

        if self.departure not in storages or self.destination not in storages:
            raise UnknownStorageError
