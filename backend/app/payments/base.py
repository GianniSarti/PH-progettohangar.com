"""Interfaccia provider-agnostica per i pagamenti (bozza, nessuna logica reale)."""

from abc import ABC, abstractmethod
from collections.abc import Mapping
from dataclasses import dataclass


@dataclass
class CheckoutSession:
    provider: str
    session_id: str
    checkout_url: str


@dataclass
class PaymentEvent:
    provider: str
    event_id: str
    event_type: str
    order_ref: str | None = None


class PaymentProvider(ABC):
    name: str

    @abstractmethod
    async def create_checkout(
        self, order_ref: str, amount_cents: int, currency: str
    ) -> CheckoutSession:
        """Crea una sessione di pagamento presso il provider."""

    @abstractmethod
    async def parse_webhook(
        self, payload: bytes, headers: Mapping[str, str]
    ) -> PaymentEvent:
        """Verifica la firma del webhook e restituisce l'evento normalizzato."""
