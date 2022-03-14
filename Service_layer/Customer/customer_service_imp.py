from Service_layer.Customer.customer_service_interface import CustomerServiceInterface
from customer_error.id_not_found import IdNotFound
from customer_error.input_length import InputLength
from customer_error.invalid_information import InvalidInformation
from dal_layer.customer.dao_customer_interface import CustomerInterfaceDao
from entities.bank_customers import Customer


class CustomerServiceImp(CustomerServiceInterface):

    def __init__(self, customer_bo: CustomerInterfaceDao):
        self.customer_bo = customer_bo


    def service_create_customer(self, customer: Customer) -> Customer:
        if type(customer.first_name) and type(customer.last_name) != str:
            raise InvalidInformation("Please insert proper information")
        elif len(customer.first_name) and len(customer.last_name) >= 20:
            raise InputLength("Your created customer is >20, please make <20.")
        return self.customer_bo.create_customer(customer)


    def service_get_customer_id(self, customer_id: int) -> Customer:
        try:
            return self.customer_bo.get_customer_id(int(customer_id))
        except ValueError:
            raise IdNotFound("This customer ID is not in our records.")

    def service_update_customer_id(self, customer: Customer) -> Customer:
        if type(customer.first_name) and type(customer.last_name) != str:
            raise InvalidInformation("Please insert proper information")
        elif len(customer.first_name) and len(customer.last_name) >= 20:
            raise InputLength("Your created customer is >20, please make <20.")
        return self.customer_bo.update_customer_id(customer)


    def service_delete_customer_id(self, customer_id) -> bool:
        if type(customer_id) == int:
            return self.customer_bo.delete_customer_id(customer_id)
        else:
            raise IdNotFound("Customer ID not found, please confirm data")
