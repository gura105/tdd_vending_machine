from functools import reduce


class Coin(object):
    def __init__(self, amount):
        self.amount = amount


class VendingMachine(object):
    def __init__(self):
        self.contained = []
        self.available_coin_amounts = [10, 50, 100, 500, 1000]

    def catch_coin(self, coin: Coin) -> Coin:
        if coin.amount in self.available_coin_amounts:
            self.contained.append(coin)
            return None
        else:
            return coin

    def coin_total(self) -> int:
        return sum([coin.amount for coin in self.contained])

    def refund(self) -> list:
        result = self.contained
        self.contained = []

        return result


class Stock(object):
    def __init__(self):
        pass
