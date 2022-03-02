from abc import ABC


class CustomerInterfaceDao(ABC):
    def create_customer(self, bankaccount: int):
        pass


class DeleteCustomerById(ABC):
    def delete_customer_by_id(self, bankaccount: int):
        pass
