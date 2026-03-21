class BankAccount:
    def __init__(self, balance):
        self._balance = balance
        
    @property
    def balance(self):
        return self._balance
    
    def deposit(self: BankAccount, amount: int):
        if amount < 0:
            raise ValueError 
        self._balance += amount

    def withdraw(self: BankAccount, amount: int):
        if amount < 0:
            raise Exception("Баланс пуст")
        if self._balance < amount:
            raise Exception("Баланс меньше снятия")

        self._balance -= amount
    
    def __str__(self):
        return f"баланс: {self._balance} руб."


bankAccount = BankAccount(0)
bankAccount.deposit(100000000)
print(bankAccount)
bankAccount.withdraw(10000)
print(bankAccount)

print(bankAccount.balance)