# from unittest import TestCase
from vending_machine.hoge.coin import Coin, VendingMachine


class TestCoin():
    def test_catch_coin(self):
        machine = VendingMachine()
        machine.catch_coin(Coin(50))
        assert Coin(50).amount == machine.contained[0].amount
