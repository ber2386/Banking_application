from abc import ABC, abstractmethod

from entities.bank_customers import Customer


class CustomerInterfaceDao(ABC):

    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get_customer_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def update_customer_id(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_customer_id(self, customer_id) -> bool:
        pass
