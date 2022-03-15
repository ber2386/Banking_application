from Tests.test_banking import account_dao
from customer_error.Negative_Value import NegativeValue
from customer_error.invalid_data import InvalidValue
from customer_error.invalid_information import InvalidInformation
from customer_error.invalid_number import InvalidNumber
from customer_error.record_not_found import RecordNotFound
from dal_layer.banking.banking_dao_imp import DaoBankingImp
from dal_layer.banking.dao_banking_interface import BankingInterfaceDao
from entities.bank_accounts import Account


class BankingServiceImp(BankingInterfaceDao):
    def __init__(self, banking_account_dao:  DaoBankingImp):
        self.banking_account_dao = banking_account_dao

    def service_create_account(self, account: Account):
        if type(account.customer_id) != int:
            raise InvalidValue("Please enter a valid customer id")
        elif type(account.balance) != int:
            raise InvalidNumber("Please enter a valid monetary value ")
        elif account.balance < 0:
            raise NegativeValue("You are trying to commit a account overdraft, enter a smaller amount")

    def service_get_account_by_id(self, account_retrieve_id: int):
        if type(account_retrieve_id) != int:
            raise RecordNotFound("Entered a Bad input please enter again")
        else:
            return self.banking_account_dao.service_get_account_by_id(account_retrieve_id)

    def service_get_all_accounts_for_user(self, customer_id: Account):
        if type(customer_id) != int:
            raise InvalidValue("Wrong value inserted, please only use numbers")
        else:
            return self.banking_account_dao.service_get_all_accounts_for_user(1)

    def service_update_account(self, account: Account):
        return account_dao.service_update_account(account)

    def service_delete_account_by_id(self, customer_id, account_id: int) -> bool:
        varify_account = account_dao.service_get_account_by_id(account_id)
        if customer_id != varify_account.customer_id:
            raise InvalidInformation("You can not close another persons account")
        return account_dao.delete_account_by_id(account_id)

    def service_withdraw_from_account_id(self, withdrawn_amount, account_id: int):
        return account_dao.service_withdraw_from_account_id(withdrawn_amount, account_id)


    def service_deposit_into_account_by_id(self, deposit_amount, account_id: int):
        return account_dao.service_deposit_into_account_by_id(deposit_amount, account_id)


    def service_transfer_money_between_accounts_by_their_ids(self, withdraw_id: int, deposit_id: int, transfer_amount):
        return account_dao.service_transfer_money_between_accounts_by_their_ids(withdraw_id, deposit_id, transfer_amount)
