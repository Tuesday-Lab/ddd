import pytest
from dateutil.parser import parse

from event.vo import Money, Schedule


@pytest.mark.parametrize("currency", ["KRW", "USD"])
@pytest.mark.parametrize("amount", [0, 100.00, 10.00])
def test_money(currency, amount):
    money = Money(currency=currency, amount=amount)

    assert money.currency == currency
    assert money.amount == amount


@pytest.mark.parametrize("currency", ["JPY"])
@pytest.mark.parametrize("amount", [10.00])
@pytest.mark.xfail(raises=ValueError)
def test_지원하지않는_통화(currency, amount):
    Money(currency=currency, amount=amount)


@pytest.mark.parametrize("currency", ["KRW"])
@pytest.mark.parametrize("amount", [-1])
@pytest.mark.xfail(raises=ValueError)
def test_금액은_0_이상(currency, amount):
    Money(currency=currency, amount=amount)


@pytest.mark.parametrize("start_time", [parse("2020-01-01 00:00:00")])
@pytest.mark.parametrize("end_time", [parse("2020-01-01 00:01:00"), parse("2020-01-20 00:00:00")])
def test_schedule(start_time, end_time):
    schedule = Schedule(start_time=start_time, end_time=end_time)

    assert schedule.start_time == start_time
    assert schedule.end_time == end_time


@pytest.mark.parametrize("start_time", [None])
@pytest.mark.parametrize("end_time", [parse("2020-01-01 00:01:00"), parse("2020-01-20 00:00:00")])
@pytest.mark.xfail(raises=ValueError)
def test_시작일없이_종료일만_있을수없음(start_time, end_time):
    schedule = Schedule(start_time=start_time, end_time=end_time)

    assert schedule.start_time == start_time
    assert schedule.end_time == end_time


@pytest.mark.parametrize("start_time", [parse("2020-02-01 00:01:00")])
@pytest.mark.parametrize("end_time", [parse("2020-01-01 00:01:00")])
@pytest.mark.xfail(raises=ValueError)
def test_시작일은_종료일_보다_작아야함(start_time, end_time):
    schedule = Schedule(start_time=start_time, end_time=end_time)

    assert schedule.start_time == start_time
    assert schedule.end_time == end_time
