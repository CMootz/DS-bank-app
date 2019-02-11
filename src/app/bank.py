import pandas as pd
import app


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = pd.DataFrame(columns=['id', 'firstname', 'lastname', 'balance'])
        self.transactions = pd.DataFrame(columns=['id', 'sender_id', 'recipient_id', 'amount',
                                                                     'subject', 'category', 'timestamp'])

    def open_account(self, *, account_id, firstname, lastname, balance=0.0):
        assert not self._has_valid_account(account_id), f'Account number {account_id} already taken!'
        account = {'id': account_id, 'firstname': firstname, 'lastname': lastname, 'balance': balance}
        self.accounts = self.accounts.append(account, ignore_index=True)
        return self.accounts

    def add_transaction(self, *, transaction_id,
                        sender_id,
                        recipient_id,
                        subject,
                        amount,
                        category,
                        timestamp):
        transaction = {'id': transaction_id, 'sender_id': sender_id, 'recipient_id': recipient_id, 'amount': amount,
                       'subject': subject, 'category': category, 'timestamp': timestamp}
        assert app.check_greater_zero(amount), 'Amount needs to be greater than 0'
        assert self._has_valid_account(sender_id), 'Sender has no account yet!'
        assert self._has_valid_account(recipient_id), 'Recipient has no account yet!'
        self.transactions = self.transactions.append(transaction, ignore_index=True)
        return self.transactions

    def _has_valid_account(self, accountnumber):
        return len(self.accounts.loc[self.accounts['id'] == accountnumber]) >= 1
