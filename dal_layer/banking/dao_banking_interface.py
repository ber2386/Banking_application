from abc import ABC, abstractmethod
from entities.bank_accounts import Account
from project_0.dal_layer.banking import banking_dao_imp

class BankingInterfaceDao(ABC):

    # create
    @abstractmethod
    def create_account(self, bankaccount: Account):
        bankaccount.account_id = self.account_id_generator
        self.account_id_generator += 1
        self.customer_list.append(bankaccount.account_id)
        return bankaccount.account_id


        # read

    @abstractmethod
    def get_account_by_id(self, bankaccount: int):
        self.customer_list = bankaccount
        pass

    # update
    @abstractmethod
    def get_all_accounts_for_user(self, bankaccount: int):
        pass

    # delete
    @abstractmethod
    def withdraw_from_account_id(self, bankaccount: int, withdraw_amount):
        pass

    @abstractmethod
    def deposit_into_account_by_id(self, bankaccount: int, deposit_amount):
        pass

    @abstractmethod
    def transfer_money_between_accounts_by_their_ids(self, bankaccount_1: int, deposit_amount, bankaccount_2):
        pass

    @abstractmethod
    def delete_account_by_id(self, bankaccount: int,):
        pass

