from src.controllers.controller import Controller
from src.payment import Payment


class PaymentControl(Controller):

    def __init__(self):
        self.payment = Payment()

    def process(self):
        pass

    def make_payment(self):
        self._do_transaction()
        invoice = self.payment.get_invoice()
        return invoice

    def _generate_invoice(self):
        self.payment._invoice = "dummy_invoice"

    def _do_transaction(self):
        self._generate_invoice()
        print("payment success")




