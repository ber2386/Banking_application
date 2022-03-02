from project_0.customer_error import id_not_found
from project_0.dal_layer.banking.banking_dao_imp import DaoBankingImp

"""This module contains customer_id dao unit tests"""

banking_dao = DaoBankingImp()
"""
create customer_id tests
business logic:
"""


def test_unique_id(self, account_id, customer_id):
    self.account_id = account_id
    self.customer_id = customer_id
    if account_id == customer_id:
        return False
    elif account_id != customer_id:
        return True
    print("Success this a unique id")


def test_customer_name(self, first, last):
    self.first = first
    self.last = last
    if first <= 20 and last <= 20:
        print("This customer is good to go")
    else:
        if first <= 20:
            print("customer is not good bad input")
        elif last <= 20:
            print("customer has bad last input")

# def test_account_balance(self, withdraw, deposit, balance):
#     if withdraw >= balance:
#         print("You are about to overdraft your account!")
#     else:
#         withdraw < balance
#     print("Please take your money and have a pleasant day")
#       elif withdraw == balance
#      print("Please take your money and have a pleasant day")


def test_check_account_input(self, bankaccount: int):
    try:
        val = int(input)
        print("input is a valid account number = ", val)
    except bankaccount:
        print("No.. this input is not a valid number it's a string")
