import requests
from protobuf_out import messages

message_to_server = messages.MessageToServer()
message_to_server.seller_data = messages.SellerProductData()
message_to_server.seller_data.product = "Water Bottles"
data_to_server = bytes(message_to_server)

res = requests.post("http://127.0.0.1:80/",
                    data=data_to_server,
                    headers={'Content-Type': 'application/octet-stream'})

list_of_relevant_customers: messages.ListRelevantCustomerData = messages.ListRelevantCustomerData().parse(res.content)
for customer in list_of_relevant_customers.relevant_customers:
    print(f"Customer product: {customer.customer_product_type}")
