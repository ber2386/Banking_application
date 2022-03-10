from customer_error.input_length import InputLength
from customer_error.record_not_found import RecordNotFound
from dal_layer.customer.customer_dao_imp import CustomerDAOImp
from entities.bank_customers import Customer
from Service_layer.Customer.customer_service_imp import CustomerServiceImp

customer_daoj = CustomerDAOImp()
customer_serj = CustomerServiceImp(customer_bo)

"""
Testing for length of ID
"""
len_first_name_creation = Customer(1, "Top", "Cat")
len_last_name_creation = Customer(2, "Yogi", "Bear")
len_first_name_improve = Customer(1, "Wally", "Gator")
len_last_name_improve = Customer(2, "Johnny", "Quest")

#Test for Type
first_name_type_creation = Customer(1,  "Top", 1)
last_name_type_creation = Customer(1,  "Cat", 1,)
first_name_type_improve = Customer(1, 1, "Johnny")
last_name_type_improve = Customer(1, 1, "Quest")

# Testing for Special ID
special_customer_id_1 = Customer(1, "Top", "Cat")
special_customer_id_2 = Customer(2, "Yogi", "Bear")


def test_check_first_name_create():
    pass


def test_check_last_name_create():
    pass


def test_check_fn_length_characters():
    pass


def test_check_ln_length_characters():
    pass


def test_check_name_combined():
    pass
