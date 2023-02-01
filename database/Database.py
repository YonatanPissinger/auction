from protobuf_out import messages
from typing import Tuple, List


class Database:
    def __init__(self):
        self._customer_requests: [messages.CustomerProductData] = []
        self._subscribers: [messages.UserData] = []

    def customer_requests(self) -> Tuple[messages.CustomerProductData, ...]:
        return tuple(self._customer_requests)

    def subscribers(self) -> Tuple[messages.UserData, ...]:
        return tuple(self._customer_requests)

    def add_customer_request(self, customer_request: messages.CustomerProductData):
        self._customer_requests.append(customer_request)

    def add_user(self, user_request: messages.UserData):
        self._subscribers.append(user_request)
