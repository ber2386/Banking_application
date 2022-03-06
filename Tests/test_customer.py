from project_0.dal_layer.banking.banking_dao_imp import DaoBankingImp
from project_0.dal_layer.customer.customer_dao_imp import CustomerDAOImp
from project_0.entities.bank_customers import Customer

customer_dao = CustomerDAOImp()

account_dao = DaoBankingImp()

new_villain = Customer(1, "Storm", "Bringer")


def test_create_customer():
    customer_dao.create_customer(new_villain)
    print(new_villain)
    assert new_villain.customer_id != 0


def test_get_customer_id():
    customer = customer_dao.get_customer_id(new_villain.customer_id)
    print(customer.customer_id)
    assert customer.customer_id == new_villain.customer_id
# If at item position 0 it fails but if changed to
#item position 1 it passes


def test_get_all_customers():
    pass


def test_update_customer():
    pass


def test_delete_customer_by_id():
    pass