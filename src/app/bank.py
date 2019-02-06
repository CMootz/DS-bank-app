import app


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def open_account(self, account):
        self._check_typus(account, 'Account', app.Account)
        message = 'Account number 1 already taken!'
        assert account.number not in self.accounts, message
        self.accounts[account.number] = account
        return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        self._check_greater_zero(amount, 'Amount')
        self._check_person_exists(sender.number, 'Sender')
        self._check_person_exists(recipient.number, 'Recipient')
        transaction = app.Transaction(sender=sender.number, recipient=recipient.number, subject=subject, amount=amount)
        assert self.accounts[sender.number].has_funds_for(amount), 'Account has not enough funds'
        self.transactions.append(transaction)
        self.accounts[sender.number].balance = self.accounts[sender.number].balance - amount
        self.accounts[recipient.number].balance = self.accounts[recipient.number].balance + amount

        return transaction

    def _check_typus(self, number, typename, typus):
        if typus is app.Account:
            message = typename + ' should be an app.Account'
        assert isinstance(number, typus), typename + message

    def _check_greater_zero(self, number, name):
        message = name + ' needs to be greater than 0'
        assert number > 0.0, message

    def _check_person_exists(self, number, name):
        message = name + ' has no account yet!'
        assert number in self.accounts, message

