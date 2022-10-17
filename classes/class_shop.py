from typing import Dict

from classes.base_class import BaseStorage
from config.exeptions import TooManyDifferentProductError


class Shop(BaseStorage):

    def __init__(self, items: Dict[str, int], capacity: int, max_items: int):
        self.max_items = max_items
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= self.max_items:
            raise TooManyDifferentProductError
        super().add(name, amount)
