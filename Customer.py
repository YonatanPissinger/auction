import json
import Client


class Customer:

    def __init__(self):
        self.customer_data = {
            "product": input("Enter your product's type please: "),
            "color": input("Enter your product's color please: "),
            "note": input("Additional comments on the product: "),

            "name": input("What is your name? "),
            "details": input("Contact Information: ")
        }

        self.dictionary_to_Json(self.customer_data)

    @staticmethod
    def dictionary_to_Json(temp_dict):
        return json.dump(temp_dict, open("out.json", "w"))


if __name__ == "__main__":
    customer = Customer()
    Client.send(customer)
    pass
