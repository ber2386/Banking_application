from Service_layer.banking_service.banking_service_interface import BankingServiceInterface
from Tests.test_banking import account_dao
from entities.bank_accounts import Account
from customer_error.invalid_number import InvalidNumber

class BankingServiceImp(BankingServiceInterface):
    def __init__(self, banking_interface_object: BankingServiceInterface):
        self.banking_interface_object = banking_interface_object



    def service_create_account(self, account: Account):
        return account_dao.create_account(account)




    def service_get_account_by_id(self, account_id: int):
        return account_dao.get_account_by_id(account_id)




    def service_get_all_accounts_for_user(self, account: Account):
        return account_dao.get_all_accounts_for_user()


    def service_update_account(self, account: Account):
        return account_dao.update_account(account)



    def service_delete_account_by_id(self, account_id: int):
        pass



    def withdraw_from_account_id(self, withdrawn_amount, account_id: int):
        if withdrawn_amount < 0:
            raise InvalidNumber("Invalid withdraw amount, negative balance")
        account = self.service_get_account_by_id(account_id)
        if withdrawn_amount > float(account.balance):
            raise InvalidNumber("Insufficient funds available in account!")
        new_balance = float(account.balance) - withdrawn_amount
        account.balance = new_balance
        return self.service_update_account(account_id, account)



    def deposit_into_account_by_id(self, deposit_amount, account_id: int):
        if deposit_amount < 0:
            raise InvalidNumber("Invalid deposit amount, negative balance")
        account = self.service_get_account_by_id(account_id)
        new_amount = float(account.balance) + deposit_amount
        account.balance = new_amount
        return self.service_update_account(account_id, account)



    def transfer_money_between_accounts_by_their_ids(self, withdraw_id: int, deposit_id: int, transfer_amount):
        pass
