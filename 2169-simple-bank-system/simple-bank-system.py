class Bank:
    def __init__(self, balance):
        self.balances = balance
        self.n = len(balance)

    def _is_valid(self, account):
        return 1 <= account <= self.n

    def transfer(self, account1, account2, money):
        if not self._is_valid(account1) or not self._is_valid(account2):
            return False
        i1, i2 = account1 - 1, account2 - 1
        if self.balances[i1] < money:
            return False
        self.balances[i1] -= money
        self.balances[i2] += money
        return True

    def deposit(self, account, money):
        if not self._is_valid(account):
            return False
        self.balances[account - 1] += money
        return True

    def withdraw(self, account, money):
        if not self._is_valid(account):
            return False
        idx = account - 1
        if self.balances[idx] < money:
            return False
        self.balances[idx] -= money
        return True