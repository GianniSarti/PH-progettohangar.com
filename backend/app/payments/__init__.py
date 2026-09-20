from app.payments.base import CheckoutSession, PaymentEvent, PaymentProvider
from app.payments.opennode_provider import OpenNodeProvider
from app.payments.stripe_provider import StripeProvider

_PROVIDERS: dict[str, type[PaymentProvider]] = {
    StripeProvider.name: StripeProvider,
    OpenNodeProvider.name: OpenNodeProvider,
}


def get_provider(name: str) -> PaymentProvider:
    try:
        return _PROVIDERS[name]()
    except KeyError:
        raise ValueError(f"Provider di pagamento sconosciuto: {name}") from None


__all__ = [
    "CheckoutSession",
    "PaymentEvent",
    "PaymentProvider",
    "OpenNodeProvider",
    "StripeProvider",
    "get_provider",
]
