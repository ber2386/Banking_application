from project_0.dal_layer.banking.banking_dao_imp import DaoBankingImp
from project_0.dal_layer.customer.customer_dao_imp import CustomerDAOImp
from project_0.entities.bank_customers import Customer

customer_dao = CustomerDAOImp()

account_dao = DaoBankingImp()


def test_create_customer():
    test_customer = Customer(0, "John", "Doe")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id


def test_get_customer_id():
    pass


def test_get_all_customers():
    pass


def test_update_customer():
    pass


def test_delete_customer_by_id():
    pass
