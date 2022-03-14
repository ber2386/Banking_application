from Tests.test_banking import account_dao
from customer_error.invalid_information import InvalidInformation
from customer_error.invalid_number import InvalidNumber
from dal_layer.banking.banking_dao_imp import DaoBankingImp
from dal_layer.banking.dao_banking_interface import BankingInterfaceDao
from entities.bank_accounts import Account


class BankingServiceImp(BankingInterfaceDao):
    def __init__(self, banking_interface_object:  DaoBankingImp):
        self.banking_interface_object = banking_interface_object

    def service_create_account(self, account: Account):
        return account_dao.create_account(account)

    def service_get_account_by_id(self, account_id: int):
        return account_dao.service_get_account_by_id(account_id)

    def service_get_all_accounts_for_user(self, account: Account):
        return account_dao.service_get_all_accounts_for_user()

    def service_update_account(self, account: Account):
        return account_dao.service_update_account(account)

    def service_delete_account_by_id(self, customer_id, account_id: int):
        varify_account = account_dao.service_get_account_by_id(account_id)
        if customer_id != varify_account.customer_id:
            raise InvalidInformation("You can not close another persons account")
        return account_dao.delete_account_by_id(account_id)

    def service_withdraw_from_account_id(self, withdrawn_amount, account_id: int):
        if withdrawn_amount < 0:
            raise InvalidNumber("Invalid withdraw amount, negative balance")
        return account_dao.service_withdraw_from_account_id(withdrawn_amount, account_id)


    def service_deposit_into_account_by_id(self, deposit_amount, account_id: int):
        if deposit_amount < 0:
            raise ValueError("Invalid deposit (negative number)")
        return account_dao.service_deposit_into_account_by_id(deposit_amount, account_id)


    def service_transfer_money_between_accounts_by_their_ids(self, withdraw_id: int, deposit_id: int, transfer_amount):
        return account_dao.service_transfer_money_between_accounts_by_their_ids(withdraw_id, deposit_id, transfer_amount)
