from Service_layer.banking_service.banking_service_imp import BankingServiceImp
from Tests.test_banking import account_dao
from customer_error.invalid_information import InvalidInformation
from customer_error.invalid_number import InvalidNumber

account_service_banking_imp = BankingServiceImp(account_dao)
"""
Negative withdraw/deposit
"""


def test_negative_withdraw():
    try:
        account_service_banking_imp.service_withdraw_from_account_id(-5, 1)
    except InvalidNumber as e:
        assert str(e) == "Invalid withdraw amount, negative balance"


def test_negative_deposit():
    try:
        account_service_banking_imp.service_deposit_into_account_by_id(-5, 1)
    except ValueError as e:
        assert str(e) == "Invalid deposit (negative number)"


def test_delete_another_customer_account():
    try:
        account_service_banking_imp.service_delete_account_by_id(2, 1)
    except InvalidInformation as e:
        assert str(e) == "You can not close another persons account"