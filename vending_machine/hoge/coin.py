
class Coin(object):
    def __init__(self, amount):
        self.amount = amount


class VendingMachine(object):
    def __init__(self):
        self.contained = []

    def catch_coin(self, coin: Coin) -> None:
        pass
