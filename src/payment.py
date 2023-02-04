class Payment:
    def __init__(self):
        self._payment_type = None
        self._invoice = None

    def set_payment_type(self, payment_type):
        self._payment_type = payment_type

    def get_invoice(self):
        return self._invoice

    def get_payment_type(self):
        return self._payment_type




