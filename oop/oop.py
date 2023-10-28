from logging import exception
import re


class BankAccount:
    def __init__(self,account_number:str,account_holder:str,initial_balance:float):

        self.accountNumber = account_number

        self.accountHolder = account_holder
        
        self.initialBalance = initial_balance

    def deposite(self,amount):

        self.initialBalance += amount    

    def withdraw(self,amount):
        
        self.initialBalance = self.initialBalance - amount

        if self.initialBalance < 0:
          raise ValueError("not sufficient balance")

    def get_balance(self):

        return self.initialBalance
    
    def display_account_info(self):

        return f"Name: {self.accountHolder}, Account no: {self.accountNumber},current balance: {self.initialBalance} " 

my_account = BankAccount('123','John Doe',1000.0)

my_account.deposite(500.0)

my_account.withdraw(200.0)

print(my_account.display_account_info())

