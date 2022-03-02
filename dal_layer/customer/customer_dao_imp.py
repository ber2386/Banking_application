from project_0.customer_error import id_not_found
from project_0.dal_layer.customer.dao_customer_interface import CustomerInterfaceDao
from project_0.entities.bank_accounts import Account

class CustomerDAOImp(CustomerInterfaceDao):
    account_list = []
    account_generator = 2
    def create_customer(self,customer, customer_id: int):
        customer.customer_id self.account_list
        self.id_generator += 1
        self.account_list.append(customer)
        return customer
