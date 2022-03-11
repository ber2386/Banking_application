from customer_error.id_not_found import IdNotFound
from customer_error.invalid_data import InvalidValue
from customer_error.record_not_found import RecordNotFound
from dal_layer.banking.dao_banking_interface import BankingInterfaceDao
from entities.bank_accounts import Account


class DaoBankingImp(BankingInterfaceDao):
    account_list = [Account(1, 0, 1250)]
    account_id_generator = 1

    def service_create_account(self, account: Account) -> Account:
        account.account_id = self.account_id_generator
        self.account_id_generator += 1
        self.account_list.append(account)
        return account

    def service_get_account_by_id(self, account_id: int) -> Account:
        for account in self.account_list:
            if account_id == account_id:
                return account
            else:
                raise IdNotFound

    def service_get_all_accounts_for_user(self, customer_id: int) -> [Account]:
        lists = []
        for account in self.account_list:
            if customer_id == account.customer_id:
                lists.append(account)
        if len(lists) > 0:
            return lists
        else:
            raise IdNotFound("No account matches the id given: please try again")

    def service_update_account(self, account: Account) -> Account:
        for old_identity in self.account_list:
            if account.account_id == old_identity.account_id:
                old_identity = account
                return old_identity
        raise IdNotFound()

    def service_delete_account_by_id(self, customer_id, account_id: int) -> bool:
        for account in self.account_list:
            if account_id == account.account_id:
                self.account_list.remove(account)
                return True
        raise IdNotFound("No customer matches the id given: please try again!")

    def service_withdraw_from_account_id(self, withdrawn_amount, account_id: int) -> Account:
        for account in self.account_list:
            if account.account_id == account_id:
                if withdrawn_amount <= account.balance:
                    account.balance -= withdrawn_amount
                    print("You have successfully withdrawn " + str(withdrawn_amount) + ".  You new balance is " + str(
                        account.balance) + ".")
                    return account

    def service_deposit_into_account_by_id(self, deposit_amount, account_id: int) -> Account:
        for account in self.account_list:
            if account_id == account.account_id:
                account.balance += deposit_amount
                print("You have successfully deposited " + str(deposit_amount) + ".  You new balance is " + str(
                    account.balance) + ".")
                return account
        raise RecordNotFound("This account was not found Please try again")

    def service_transfer_money_between_accounts_by_their_ids(self, from_account: int, to_account: int,
                                                             transfer_amount: float):
        withdraw_account = Account(1, 1, 1)
        deposit_account = Account(1, 1, 1)
        for account in self.account_list:
            if account.account_id == from_account:
                withdraw_account = account
            if account.customer_id == to_account:
                deposit_account = account

        if withdraw_account.balance - transfer_amount < 0:
            raise InvalidValue("This puts you in the negative")
        else:
            withdraw_account.balance = withdraw_account.balance - transfer_amount
            deposit_account.balance = deposit_account.balance + transfer_amount
            return deposit_account.balance
