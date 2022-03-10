from Service_layer.Customer.customer_service_interface import CustomerServiceInterface
from entities.bank_customers import Customer
from dal_layer.customer.dao_customer_interface import CustomerInterfaceDao
from customer_error.id_not_found import IdNotFound
from customer_error.invalid_number import InvalidNumber
class CustomerServiceImp(CustomerServiceInterface):

    def __init__(self, customer_bo: CustomerInterfaceDao):
        self.customer_bo = customer_bo

    def service_create_customer(self, customer: Customer) -> Customer:
        # This is our first, last name and combined first/last name
        pass

    def service_get_customer_id(self, customer_id: int) -> Customer:
        try:
            return self.customer_bo.get_customer_id(int(customer_id))
        except ValueError:
            raise IdNotFound("This customer ID is not in our records.")

    def service_update_customer_id(self, customer: Customer) -> Customer:
        pass

    def service_delete_customer_id(self, customer_id) -> bool:
        if type(customer_id) == int:
            return self.customer_bo.delete_customer_id(customer_id)
        else:
            raise IdNotFound("Customer ID not found, please confirm data")
