class Account:
    '''
    A simple bank account
    '''

    def __init__(self, owner:str, balance:float):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f'Account({self.owner!r}, {self.balance!r})'

    def deposit(self, amount:float):
        self.balance += amount

    def withdraw(self, amount:float):
        self.balance -= amount

    def inquiry(self) -> float:
        return self.balance


class AccountPortfolio:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def total_funds(self):
        return sum(account.inquiry() for account in self.accounts)

    def __len__(self):
        return len(self.accounts)

    def __getitem__(self, index):
        return self.accounts[index]

    def __iter__(self):
        return iter(self.accounts)


if __name__=='__main__':
    port = AccountPortfolio()
    port.add_account(Account('Guido', 1000.0))
    port.add_account(Account('Eva', 50.0))

    print(port.total_funds())  # -> 1050.0
    len(port)  # -> 2
for account in port:
    print(account)
