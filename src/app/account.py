from datetime import datetime


class Account:
    def __init__(self, *, firstname, lastname, number=0, balance=0.0):
        self.firstname = firstname
        self.lastname = lastname
        assert isinstance(number, int), 'Number needs to be an integer'
        if isinstance(number, int):
            self.number = number
        assert isinstance(balance, float), 'Balance needs to be a float'
        if isinstance(balance, float):
            self.balance = balance
        self.dtlaststatement = datetime.now()

    def info(self):
        return 'Number ' + str(self.number) + ': ' + self.firstname + ' ' + self.lastname + ' - ' + str(self.balance) +\
               ' €'

    def has_funds_for(self, amount):
        return self.balance >= amount

    def add_to_balance(self, amount):
        message = 'Amount needs to be greater than 0'
        assert amount > 0, message
        self.balance = self.balance + amount

    def subtract_from_balance(self, amount):
        message = 'Account has not enough funds'
        assert self.has_funds_for(amount), message
        self.balance = self.balance - amount
