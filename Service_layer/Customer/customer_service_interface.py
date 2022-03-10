from abc import ABC, abstractmethod

from entities.bank_customers import Customer


class CustomerServiceInterface(ABC):

    @abstractmethod
    def service_create_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_update_customer_id(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer_id(self, customer_id) -> bool:
        pass
