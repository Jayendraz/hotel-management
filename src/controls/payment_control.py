from src.controls.control import Control
from src.payment import Payment


class PaymentControl(Control):

    def __init__(self):
        self.payment = Payment()

    def process(self):
        pass

    def make_payment(self):
        payment_status = self._do_transaction()
        if payment_status == "success":
            invoice = self.payment.get_invoice()
            return invoice
        else:
            return None

    def _generate_invoice(self):
        self.payment._invoice = "dummy_invoice"

    def _do_transaction(self):
        self._generate_invoice()
        return "success"




