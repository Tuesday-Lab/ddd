import pytest

from event.vo import Money


@pytest.mark.parametrize("currency", ["KRW", "USD"])
@pytest.mark.parametrize("amount", [0, 100.00, 10.00])
def test_money(currency, amount):
    money = Money(currency=currency, amount=amount)

    assert money.currency == currency
    assert money.amount == amount


@pytest.mark.parametrize("currency", ["JPY"])
@pytest.mark.parametrize("amount", [-1])
@pytest.mark.xfail(raises=ValueError)
def test_money(currency, amount):
    Money(currency=currency, amount=amount)
