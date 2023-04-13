class BankAccount:

    def __init__(self, int_rate=0.01 ,balance=0): 
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("ERRO: You do not have enough money to withdrawl")
            self.balance-=5
            return self
        else:
            self.balance -= amount
            return self
        
    def display_account_info(self):
        print("Balance: $"+ str(self.balance))
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance*=(self.int_rate+1)
        return self


class User:
    def __init__(self,username,lastname):
        self.username = username
        self.lastname= lastname
        self.account=BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        print("User: "+self.username+", Balance: $"+str(self.account.balance))
        return self


    """def transfer_money(self, other_user, amount):
        if amount > self.balance:
            print("ERRO: You do not have enough money to withdrawl")
            return self
        else:
            self.balance -= amount
            other_user.balance += amount
            print("Transfer succeeds! Now:")
            self.display_user_balance()
            other_user.display_user_balance()
            return self"""


user1 = User("Xhoni", "Toromeni")

user2 = User("Endi", "mhvm")
user3 = User("Klea", "hghv")


user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(350).display_user_balance()

#user2.make_deposit(50).make_deposit(10).make_withdrawal(290).make_withdrawal(666).display_user_balance()

#user3.make_deposit(10).make_withdrawal(9).make_withdrawal(2).make_withdrawal(4).display_user_balance()

#user1.transfer_money(user3,100)
#user1=BankAccount(0.01,825)
#user2=BankAccount(0.01,790)

