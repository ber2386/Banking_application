from customer_error.id_not_found import IdNotFound
from customer_error.record_not_found import RecordNotFound
from dal_layer.banking.banking_dao_imp import DaoBankingImp
from entities.bank_accounts import Account

account_dao = DaoBankingImp()

testing_account = Account(1, 1, 1750)
account_dao.service_create_account(testing_account)
create_account = (Account(2, 2, 2))

"""
Business logic:
    Accounts may not have the same unique_id=account_id (This will be handled on service layer)
    Accounts can't have a negative balance, check for sufficient funds for a withdraw and to transfer between
    two Accounts.
"""

"""
Here I will check that the correct data is provided to the method intended, 
and that the method returns the expected return value.
In addition to check and make sure data exists and to return a message if it does not
"""

"""
Tests for creating an account
"""


def test_create_account_successfully():
    account_dao.service_create_account(testing_account)
    print(testing_account)
    assert testing_account.account_id != 0


def test_non_unique_account_id():
    test_account = Account(1, 225, 1)
    result = account_dao.service_create_account(test_account)
    assert result.account_id != 1


"""
Read account tests
"""


def test_get_account_by_id_successfully():
    account_dao.service_get_account_by_id(testing_account.account_id)
    assert testing_account.account_id == 2


def test_get_account_by_id_not_found():
    try:
        account_dao.service_get_account_by_id(0)
        assert True

    except RecordNotFound as e:
        assert str(e) == "No account matches query, try again!"


def test_get_all_accounts_for_user():
    result = account_dao.service_get_all_accounts_for_user(0)
    assert result[0].customer_id == 0


"""
Update account tests
"""


def test_update_account():
    testing_account.account_value = 5.25
    updated_account = account_dao.service_update_account(testing_account)
    print(updated_account)


"""
Withdraw tests/deposit tests
"""


def test_deposit_into_account_by_id():
    result = account_dao.service_deposit_into_account_by_id(500, 1)
    assert result.balance == 1750


def test_withdraw_from_account_id():
    result = account_dao.service_withdraw_from_account_id(1000, 1)
    assert result.balance == 750


"""
Transfer test
"""


def test_transfer_between_accounts():
    result = account_dao.service_transfer_money_between_accounts_by_their_ids(1, 2, 502)
    assert result == 503


"""
Delete account tests
"""


def test_delete_account_by_id():
    result = account_dao.service_delete_account_by_id(1, 2)
    assert result is True


def test_delete_account_by_id_no_match():
    try:
        account_dao.service_delete_account_by_id(3, 1)
    except IdNotFound as e:
        assert str(e) == "This ID was not found in our database please try again"
