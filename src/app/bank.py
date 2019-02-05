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

        sendervorhanden = 0
        for item in self.accounts:
            if item['number'] == sender['number']:
                sendervorhanden = 1
        assert sendervorhanden == 1, 'Sender has no account yet!'

        empfvorhanden = 0
        for item in self.accounts:
            if item['number'] == recipient['number']:
                empfvorhanden = 1
        assert empfvorhanden == 1, 'Recipient has no account yet!'

        self.transactions.append(transaction)
        return transaction
