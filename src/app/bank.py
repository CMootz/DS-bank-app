import app
from datetime import datetime


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.transactions = []

    def open_account(self, account):
        self._check_typus(account, 'Account', app.Account)
        message = 'Account number %s already taken!' % str(account.number)
        assert account.number not in self.accounts, message
        self.accounts[account.number] = account
        return account

    def add_transaction(self, *, sender, recipient, subject, amount):
        self._check_greater_zero(amount, 'Amount')
        self._check_account_exists(sender.number, 'Sender')
        self._check_account_exists(recipient.number, 'Recipient')
        assert sender.has_funds_for(amount), 'Account has not enough funds'
        transaction = app.Transaction(sender=sender.number, recipient=recipient.number, subject=subject, amount=amount)
        self.transactions.append(transaction)
        sender.subtract_from_balance(amount)
        recipient.add_to_balance(amount)
        return transaction

    def _build_transactionlist_for_account(self, accountnumber):
        assert len(self.accounts) > 0 and isinstance(self.transactions[0], app.Transaction), 'Die Transaktionslist ' \
                                                                                             'hat keine Einträge oder' \
                                                                                             ' hat den falschen Typ'
        filtered = filter(lambda acc: acc.sender == accountnumber or acc.recipient == accountnumber, self.transactions)
        return list(filtered)

    def _filter_transactionlist_for_account_bydates(self, date_start, date_end, flist):
        filtered = filter(lambda transact: transact.timestamp.date() >= date_start, flist)
        filtered = filter(lambda transact: transact.timestamp.date() <= date_end, filtered)
        return list(filtered)

    def print_bankstatement_all(self, accountnumber):
        transactionlist = self._build_transactionlist_for_account(accountnumber)
        transactionlist.sort(key=lambda transact: transact.timestamp.date())

        print(f' Konto-Nr: {accountnumber}')
        print(f' {self.name}')

        value_old = self.accounts[accountnumber].balance
        for item in transactionlist:
            if item.sender == accountnumber:
                value_old = value_old + item.amount
            if item.recipient == accountnumber:
                value_old = value_old - item.amount
        print(' Kontostand in EUR am {day:02d}.{month:02d}.{year:04d} {hour:02d}:{minute:02d}{old:>50.2f}'
              .format(day=self.accounts[accountnumber].dtlaststatement.day,
                      month=self.accounts[accountnumber].dtlaststatement.month,
                      year=self.accounts[accountnumber].dtlaststatement.year,
                      hour=self.accounts[accountnumber].dtlaststatement.hour,
                      minute=self.accounts[accountnumber].dtlaststatement.minute,
                      old=value_old))
        for item in transactionlist:
            if item.sender == accountnumber:
                print(' {day:02d}.{month:02d}   {subject:<20s}{firstname:>20s} {lastname:20s}'
                      '{amount:> 18.2f}'.format(day=item.timestamp.day, month=item.timestamp.month, subject=item.subject,
                                           firstname=self.accounts[item.recipient].firstname,
                                           lastname=self.accounts[item.recipient].lastname,
                                           amount=-item.amount))
            if item.recipient == accountnumber:
                print(' {day:02d}.{month:02d}   {subject:<20s}{firstname:>20s} {lastname:20s}'
                      '{amount:> 18.2f}'.format(day=item.timestamp.day, month=item.timestamp.month, subject=item.subject,
                                           firstname=self.accounts[item.sender].firstname,
                                           lastname=self.accounts[item.sender].lastname,
                                           amount=item.amount))
        actualdt = datetime.now()
        print(' Kontostand in EUR am {day:02d}.{month:02d}.{year:04d} {hour:02d}:{minute:02d}{balance:>50.2f}'
        .format(day=actualdt.day,
                month=actualdt.month,
                year=actualdt.year,
                hour=actualdt.hour,
                minute=actualdt.minute,
                balance=self.accounts[accountnumber].balance))

    def print_bankstatement_time(self, accountnumber, date_start, date_end):
        transactionlist = self._build_transactionlist_for_account(accountnumber)
        transactionlist_timespan = self._filter_transactionlist_for_account_bydates(date_start.date(), date_end.date(), transactionlist)
        actualdt = datetime.now()
        transactionlist_now2end = self._filter_transactionlist_for_account_bydates(date_end.date(), actualdt.date(), transactionlist)

        transactionlist_timespan.sort(key=lambda transact: transact.timestamp.date())

        print(f' Konto-Nr: {accountnumber}')
        print(f' {self.name}')

        value_old = self.accounts[accountnumber].balance
        for item in transactionlist_now2end:
            if item.sender == accountnumber:
                value_old = value_old + item.amount
            if item.recipient == accountnumber:
                value_old = value_old - item.amount
        balance_at_end = value_old

        for item in transactionlist_timespan:
            if item.sender == accountnumber:
                value_old = value_old + item.amount
            if item.recipient == accountnumber:
                value_old = value_old - item.amount
        print(' Kontostand in EUR am {day:02d}.{month:02d}.{year:04d} {hour:02d}:{minute:02d}{old:>50.2f}'
              .format(day=date_start.day,
                      month=date_start.month,
                      year=date_start.year,
                      hour=date_start.hour,
                      minute=date_start.minute,
                      old=value_old))
        for item in transactionlist_timespan:
            if item.sender == accountnumber:
                print(' {day:02d}.{month:02d}   {subject:<20s}{firstname:>20s} {lastname:20s}'
                      '{amount:> 18.2f}'.format(day=item.timestamp.day, month=item.timestamp.month, subject=item.subject,
                                           firstname=self.accounts[item.recipient].firstname,
                                           lastname=self.accounts[item.recipient].lastname,
                                           amount=-item.amount))
            if item.recipient == accountnumber:
                print(' {day:02d}.{month:02d}   {subject:<20s}{firstname:>20s} {lastname:20s}'
                      '{amount:> 18.2f}'.format(day=item.timestamp.day, month=item.timestamp.month, subject=item.subject,
                                           firstname=self.accounts[item.sender].firstname,
                                           lastname=self.accounts[item.sender].lastname,
                                           amount=item.amount))
        print(' Kontostand in EUR am {day:02d}.{month:02d}.{year:04d} {hour:02d}:{minute:02d}{balance:>50.2f}'
        .format(day=date_end.day,
                month=date_end.month,
                year=date_end.year,
                hour=date_end.hour,
                minute=date_end.minute,
                balance=balance_at_end))

    def _check_typus(self, number, typename, typus):
        if typus is app.Account:
            message = typename + ' should be an app.Account'
        assert isinstance(number, typus), typename + message

    def _check_greater_zero(self, number, name):
        message = name + ' needs to be greater than 0'
        assert number > 0.0, message

    def _check_account_exists(self, number, name):
        message = name + ' has no account yet!'
        assert number in self.accounts, message
