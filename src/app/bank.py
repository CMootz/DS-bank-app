class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []

    def open_account(self, account):
        for item in self.accounts:
            assert item['number'] != account['number'], 'Account number 1 already taken!'
        self.accounts.append(account)
        return self.accounts[-1]

    def add_transaction(self, *, sender, recipient, subject, amount):
        transaction = {'sender': sender,
                       'recipient': recipient,
                       'subject': subject,
                       'amount': amount}
        message = 'Amount has to be greater than 0'
        assert amount > 0, message

        senderexists = 0
        for item in self.accounts:
            if item['number'] == sender['number']:
                senderexists = 1
        assert senderexists == 1, 'Sender has no account yet!'

        recipientexists = 0
        for item in self.accounts:
            if item['number'] == recipient['number']:
                recipientexists = 1
        assert recipientexists == 1, 'Recipient has no account yet!'

        self.transactions.append(transaction)
        return transaction
