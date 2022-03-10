from abc import abstractmethod, ABC
from entities.bank_accounts import Account

class BankingServiceInterface(ABC):

    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        pass


    @abstractmethod
    def service_get_account_by_id(self, account_id: int) -> Account:
        pass


    @abstractmethod
    def service_get_all_accounts_for_user(self, account: Account) -> Account:
        pass


    @abstractmethod
    def service_update_account(self, account: Account) -> Account:
        pass


    @abstractmethod
    def service_delete_account_by_id(self, account: int) -> bool:
        pass


    @abstractmethod
    def withdraw_from_account_id(self, withdrawn_amount, account_id: int) -> Account:
        pass


    @abstractmethod
    def deposit_into_account_by_id(self, deposit_amount, account_id: int) -> Account:
        pass


    @abstractmethod
    def transfer_money_between_accounts_by_their_ids(self, withdraw_id: int, deposit_id: int, transfer_amount) -> bool:
        pass