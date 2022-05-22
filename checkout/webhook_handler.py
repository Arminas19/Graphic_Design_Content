from django.http import HttpResponse

class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """  Handle a generic/unknown/unexpected webhook event. """

        return HttpResponse(
            content=f'unhandled webhook recived: {event["type"]}',
            status=200)
    
    def Handle_payment_intent_succeeded(self, event):
        """  Handle the payment_intent.succeeded webhook from stripe. """

        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200)

    def Handle_payment_intent_payment_failed(self, event):
        """  Handle the payment_intent.payment_failed webhook from stripe. """

        return HttpResponse(
            content=f'Payment Failed Webhook recived: {event["type"]}',
            status=200)