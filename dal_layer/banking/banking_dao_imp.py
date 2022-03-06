from abc import ABC

from project_0.customer_error.id_not_found import IdNotFound
from project_0.dal_layer.banking.dao_banking_interface import BankingInterfaceDao
from project_0.entities.bank_accounts import Account


class DaoBankingImp(BankingInterfaceDao, ABC):
    account_list = [Account(1, 0, 1)]
    account_id_generator = 2

    def create_account(self, account: Account) -> Account:
        account.account_id = self.account_id_generator
        self.account_id_generator += 1
        self.account_list.append(account)
        return account


    def get_account_by_id(self, account_id: int) -> Account:
        for account in self.account_list:
            if account_id == account_id:
                return account
            else:
                raise IdNotFound

    def get_all_accounts_for_user(self, account: Account) -> Account:
        for account_id in self.account_list:
            if account.account_id == account_id:
                return account_id
        raise IdNotFound("No account matches the id given: please try again")


    def update_account(self, account: Account) -> Account:
        for old_identity in self.account_list:
            if account.account_id == old_identity.account_id:
                old_identity = account
                return old_identity
        raise IdNotFound()


    def delete_account_by_id(self, account: int) -> bool:
        for account in self.account_list:
            if self.account_list == account:
                self.account_list.remove(account)
                return True
        raise IdNotFound("No customer matches the id given: please try again!")

    def withdraw_from_account_id(self, account_id: int) -> Account:
        pass



    def deposit_into_account_by_id(self, account_id: int) -> Account:
        pass