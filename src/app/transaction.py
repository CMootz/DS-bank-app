class Transaction:
    def __init__(self, *, sender, recipient, subject, amount):

        self._check_typus(sender, 'Sender', int)
        self.sender = sender
        self._check_typus(recipient, 'Recipient', int)
        self.recipient = recipient
        self.subject = subject
        self._check_typus(amount, 'Amount', float)
        self._check_greater_zero(amount, 'Amount')
        self.amount = amount

    def _check_typus(self, number, typename, typus):
        if typus is int:
            message = typename + ' needs to be an integer'
        if typus is float:
            message = typename + ' needs to be a float'
        assert isinstance(number, typus), typename + message

    def _check_greater_zero(self, number, name):
        message = name + ' needs to be greater than 0'
        assert number > 0, message

    def info(self):
        return 'From ' + str(self.sender) + ' to ' + str(self.recipient) + ': ' + self.subject + ' - ' + \
               str(self.amount) + ' €'
