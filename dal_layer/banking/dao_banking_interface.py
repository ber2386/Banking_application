from abc import ABC, abstractmethod
from project_0.entities.bank_accounts import Account


class BankingInterfaceDao(ABC):

    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def get_all_accounts_for_user(self, account: Account) -> Account:
        pass

    @abstractmethod
    def update_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def delete_account_by_id(self, account: int) -> bool:
        pass

    @abstractmethod
    def withdraw_from_account_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def deposit_into_account_by_id(self, account_id: int) -> Account:
        pass