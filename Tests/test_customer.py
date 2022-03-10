from dal_layer.banking.banking_dao_imp import DaoBankingImp
from dal_layer.customer.customer_dao_imp import CustomerDAOImp
from entities.bank_customers import Customer

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


def test_get_all_customers():
    villain1 = Customer(0, "Sound", "Wave")
    villain2 = Customer(0, "Cobra", "Commander")
    villain3 = Customer(0, "Dr.", "Claw")
    customer_dao.create_customer(villain1)
    customer_dao.create_customer(villain2)
    customer_dao.create_customer(villain3)
    pass


def test_update_customer():
    new_villain.first_name = "Fight"
    print(new_villain)
    updated_villain = customer_dao.update_customer_id(new_villain)
    print(new_villain)
    assert updated_villain.first_name == new_villain.first_name


def test_delete_customer_by_id():
    result = customer_dao.delete_customer_id(new_villain.customer_id)
    print(result)
