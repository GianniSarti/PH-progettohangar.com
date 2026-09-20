from collections.abc import Mapping

from app.payments.base import CheckoutSession, PaymentEvent, PaymentProvider


class OpenNodeProvider(PaymentProvider):
    """Stub (provider inattivo): nessuna logica reale, nessuna chiave."""

    name = "opennode"

    async def create_checkout(
        self, order_ref: str, amount_cents: int, currency: str
    ) -> CheckoutSession:
        raise NotImplementedError

    async def parse_webhook(
        self, payload: bytes, headers: Mapping[str, str]
    ) -> PaymentEvent:
        raise NotImplementedError
