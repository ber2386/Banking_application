from abc import ABC
from project_0.customer_error.id_not_found import IdNotFound
from project_0.dal_layer.banking.dao_banking_interface import BankingInterfaceDao
from project_0.entities.bank_accounts import Account


class DaoBankingImp(BankingInterfaceDao, ABC):
    customer_list = []
    account_id_generator = 2

    def __init__(self, customer):
        customer_id_return = customer(1, "Black Knight")
        self.customer_list.append(customer_id_return)

    def create_account(self, bankaccount: Account):
        bankaccount.account_id = self.account_id_generator
        self.account_id_generator += 1
        self.customer_list.append(bankaccount.account_id)
        return bankaccount.account_id


def get_account_by_id(self, bankaccount: int):
    self.customer_list = bankaccount
    self.account_id_generator = 2
    pass


def get_all_accounts_for_user(self, bankaccount: int):
    pass


# def service_withdraw(value, account_id):
# 	return dao.withdraw_method(value, account_id)
#
    # def service_deposit(value, account_id):
    #     return dao.deposite_method(value, account_id)


def transfer_money_between_accounts_by_their_ids(self, bankaccount_1: int, deposit_amount, bankaccount_2):
    pass


def delete_account_by_id(self, bankaccount: int):
    for customer in self.customer_list:
        if customer.customer_list == bankaccount:
            self.customer_list.remove(customer)
            return True
    raise IdNotFound("No customer matches the id given: please try again!")


def update_customer_id(self, customer_id):
    for customer_id in self.customer_list:
        if customer_id == customer_id:
            customer = customer_id
            return customer
    raise IdNotFound("No customer_id matches the id given: please try again!")
