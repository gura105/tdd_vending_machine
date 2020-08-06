from unittest import TestCase


class CoinTest(TestCase):
    def test_catch_coin(self):
        machine = VendingMachine()
        machine.get_coin(Coin(50): Coin)
        assert([Coin(50).amount, machine.contained[0].amount)
