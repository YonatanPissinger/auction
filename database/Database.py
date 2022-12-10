from protobuf_out import messages
from typing import Tuple, List


class Database:
    def __init__(self):
        self._customer_requests: [messages.CustomerData] = []

    # Create getter that returns a deep-copy tuple of the list
    # with a type hint of a tuple whose elements are all of type CustomerData
    def customer_requests(self) -> Tuple[messages.CustomerData, ...]:
        return tuple(self._customer_requests)

    def add_customer_request(self, customer_request: messages.CustomerData):
        self._customer_requests.append(customer_request)
