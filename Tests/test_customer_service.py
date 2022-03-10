from Service_layer.Customer.customer_service_imp import CustomerServiceImp
from customer_error.input_length import InputLength
from customer_error.invalid_information import InvalidInformation
from dal_layer.customer.customer_dao_imp import CustomerDAOImp
from entities.bank_customers import Customer

"""
Test customers
"""
customer_bo = CustomerDAOImp()
customer_boj = CustomerServiceImp(customer_bo)
customer_first_name_to_long = Customer(1, "Teenage Mutant Turtles", "frolicked")
customer_last_name_to_long = Customer(2, "george", "RedGreenOrangesKiwis")
"""
Testing for Type
"""
first_name_type_creation = Customer(1, "Top", "Jerry")
last_name_type_creation = Customer(1, "Cat", "Mouse", )
first_name_type_improve = Customer(1, "Fred", "Johnny")
last_name_type_improve = Customer(1, "Burger", "Quest")

"""
Testing for length of ID
"""
len_first_name_creation = Customer(1, "Top", "Cat")
len_last_name_creation = Customer(2, "Yogi", "Bear")
len_first_name_improve = Customer(1, "Wally", "Gator")
len_last_name_improve = Customer(2, "Johnny", "Quest")

"""
Testing for Unique ID
"""
special_customer_id_1 = Customer(1, "Top", "Cat")
"""
Testing Name Creation
"""


def test_check_first_name_create():
    try:
        customer_boj.service_create_customer(first_name_type_creation)
    except InputLength as e:
        assert str(e) == "This First name is to long"


def test_check_last_name_create():
    try:
        customer_boj.service_create_customer(last_name_type_creation)
    except InputLength as e:
        assert str(e) == "This Last name is to long"


"""
Testing name being unique 
"""


def test_ck_unique_first_name():
    try:
        customer_boj.service_update_customer_id(special_customer_id_1)
    except InvalidInformation as e:
        assert str(e) == "Please insert authentic information"


def test_ck_unique_last_name():
    try:
        customer_boj.service_update_customer_id(special_customer_id_1)
    except InvalidInformation as e:
        assert str(e) == "Please insert authentic information"


"""
Checking the length of the names
"""


def test_check_fn_length_characters():
    try:
        customer_boj.service_create_customer(len_first_name_improve)
        assert True
    except InputLength as e:
        assert e
        assert str(e) == "Your first name is over 20 characters"


def test_check_ln_length_characters():
    try:
        customer_boj.service_create_customer(len_last_name_improve)
    except InputLength as e:
        assert e
        assert str(e) == "Your first name is over 20 characters"





