from project_0.dal_layer.banking.banking_dao_imp import DaoBankingImp
from project_0.entities.bank_accounts import Account
"""This module contains customer_id dao unit tests"""

"""
create customer_id tests
business logic:
"""
account_dao = DaoBankingImp()


def test_unique_id():
    test_account = Account(2, 554, 500)
    result = account_dao.create_account(test_account)
    assert result.account_id != 1


def test_create_account():
    pass


def test_get_account_by_id():
    pass


def test_get_all_accounts_for_user():
    pass


def test_update_account():
    pass


def test_delete_account_by_id():
    pass


def test_account_balance():
    pass


def test_withdraw_from_account_id():
    pass


def test_withdraw_overdraft():
    pass


def test_deposit_into_account_by_id():
    pass


def test_negative_deposit():
    pass


def test_transfer_between_accounts():
    pass


def test_sufficient_transfer_funds():
    pass
