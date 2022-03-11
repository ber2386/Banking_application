from abc import ABC, abstractmethod
from entities.bank_accounts import Account


class BankingInterfaceDao(ABC):

    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_get_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def service_get_all_accounts_for_user(self, customer_id: int) -> [Account]:
        pass

    @abstractmethod
    def service_update_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_delete_account_by_id(self, customer_id, account_id: int) -> bool:
        pass

    @abstractmethod
    def service_withdraw_from_account_id(self, withdrawn_amount, account_id: int) -> Account:
        pass

    @abstractmethod
    def service_deposit_into_account_by_id(self,deposit_amount, account_id: int) -> Account:
        pass

    @abstractmethod
    def service_transfer_money_between_accounts_by_their_ids(self, withdraw_id: int, deposit_id: int, transfer_amount) -> bool:
        pass
