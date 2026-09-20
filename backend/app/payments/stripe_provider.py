from collections.abc import Mapping

from app.payments.base import CheckoutSession, PaymentEvent, PaymentProvider


class StripeProvider(PaymentProvider):
    """Stub: nessuna logica reale, nessuna chiave."""

    name = "stripe"

    async def create_checkout(
        self, order_ref: str, amount_cents: int, currency: str
    ) -> CheckoutSession:
        raise NotImplementedError

    async def parse_webhook(
        self, payload: bytes, headers: Mapping[str, str]
    ) -> PaymentEvent:
        raise NotImplementedError
