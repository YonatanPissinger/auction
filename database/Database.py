from protobuf_out import messages
from typing import Tuple, List


class Database:
    def __init__(self):
        self._users: [messages.NewUserData] = []
        self._products_list: [messages.CustomerProductData] = []
        self._relevant_products_to_seller: [messages.CustomerProductData] = []

    def UsersListToTuple(self) -> Tuple[messages.NewUserData, ...]:
        return tuple(self._users)

    def ProductListToTuple(self) -> Tuple[messages.CustomerProductData, ...]:
        return tuple(self._products_list)

    def RelevantProductsToSellerListToTuple(self) -> Tuple[messages.CustomerProductData, ...]:
        return tuple(self._relevant_products_to_seller)

    def AddUser(self, user: messages.NewUserData):
        self._users.append(user)

    def AddProduct(self, product: messages.CustomerProductData):
        self._products_list.append(product)

    def RemoveProduct(self, ProductIndex):
        self._products_list.remove(ProductIndex)

    def AddMatchingProduct(self, product: messages.CustomerProductData):
        self._relevant_products_to_seller.append(product)
