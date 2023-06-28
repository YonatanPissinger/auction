# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: messages.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class NewUserData(betterproto.Message):
    user_name: str = betterproto.string_field(1)
    user_password: str = betterproto.string_field(2)
    user_phone_number: str = betterproto.string_field(3)
    user_status: str = betterproto.string_field(4)


@dataclass
class OldUserData(betterproto.Message):
    user_name: str = betterproto.string_field(1)
    user_password: str = betterproto.string_field(2)


@dataclass
class CustomerProductData(betterproto.Message):
    user_name: str = betterproto.string_field(1)
    user_phone_number: str = betterproto.string_field(2)
    customer_product_type: str = betterproto.string_field(3)
    customer_note: str = betterproto.string_field(4)


@dataclass
class SellerProductData(betterproto.Message):
    seller_product_type: str = betterproto.string_field(1)


@dataclass
class MessageToServer(betterproto.Message):
    new_user_data: "NewUserData" = betterproto.message_field(
        1, group="StructMessageToServer"
    )
    old_user_data: "OldUserData" = betterproto.message_field(
        2, group="StructMessageToServer"
    )
    customer_product_data: "CustomerProductData" = betterproto.message_field(
        3, group="StructMessageToServer"
    )
    seller_product_data: "SellerProductData" = betterproto.message_field(
        4, group="StructMessageToServer"
    )


@dataclass
class MessageToUser(betterproto.Message):
    success: "ServerSuccess" = betterproto.message_field(1, group="StructMessageToUser")
    is_exist: "SignUpProblem" = betterproto.message_field(
        2, group="StructMessageToUser"
    )
    incorrect_data: "SignInProblem" = betterproto.message_field(
        3, group="StructMessageToUser"
    )
    server_error: "ServerError" = betterproto.message_field(
        4, group="StructMessageToUser"
    )
    full_user_data: "NewUserData" = betterproto.message_field(
        5, group="StructMessageToUser"
    )
    list_relevant_customer_data: "ListRelevantCustomerData" = betterproto.message_field(
        6, group="StructMessageToUser"
    )


@dataclass
class ServerSuccess(betterproto.Message):
    additional_information: str = betterproto.string_field(1)


@dataclass
class SignUpProblem(betterproto.Message):
    user_name_exist: str = betterproto.string_field(1)


@dataclass
class SignInProblem(betterproto.Message):
    user_name_or_password_incorrect: str = betterproto.string_field(1)


@dataclass
class ServerError(betterproto.Message):
    error_message: str = betterproto.string_field(1)


@dataclass
class ListRelevantCustomerData(betterproto.Message):
    relevant_customers: List["CustomerProductData"] = betterproto.message_field(1)
