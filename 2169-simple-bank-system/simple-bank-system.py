class Bank:

    def __init__(self, balance: List[int]):
        self.dic = {}
        for i in range(1, len(balance) + 1):
            self.dic[i] = balance[i - 1]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.dic and account2 in self.dic and self.dic[account1] >= money:
            self.dic[account1] -= money
            self.dic[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.dic:
            self.dic[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.dic and self.dic[account] >= money:
            self.dic[account] -= money
            return True
        return False