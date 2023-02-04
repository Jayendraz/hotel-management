class Payment:
    def __init__(self):
        self._payment_type = None
        self.invoice = None

    def _generate_invoice(self):
        return "invoice generated"

    def set_payment_type(self, payment_type):
        self._payment_type = payment_type

    def get_payment_type(self):
        return self._payment_type

    def do_payment(self):
        self._generate_invoice()
        return "payment success"




