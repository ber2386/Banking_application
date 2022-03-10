from customer_error.id_not_found import IdNotFound
from dal_layer.customer.dao_customer_interface import CustomerInterfaceDao
from entities.bank_customers import Customer


class CustomerDAOImp(CustomerInterfaceDao):

    def __init__(self):
        customer_id_catch = Customer(1, "Black", "Knight")
        self.customer_list = []
        self.customer_id_generator = 2
        self.customer_list.append(customer_id_catch)

    def create_customer(self, customer: Customer) -> Customer:
        customer.customer_id = self.customer_list
        self.customer_id_generator += 1
        self.customer_list.append(customer)
        return customer

    def get_customer_id(self, customer_id: int) -> Customer:
        for customer in self.customer_list:
            if customer.customer_id == customer_id:
                return customer
        raise IdNotFound("No Customer id found in our system!")

    def update_customer_id(self, customer: Customer) -> Customer:
        for old_identity in self.customer_list:
            if customer.customer_id == old_identity.customer_id:
                old_identity = customer
                return old_identity
        raise IdNotFound

    def delete_customer_id(self, customer_id) -> bool:
        for customer in self.customer_list:
            if customer.customer_id == customer_id:
                self.customer_list.remove(customer)
                return True
        raise IdNotFound("No customer id found, please try again")
