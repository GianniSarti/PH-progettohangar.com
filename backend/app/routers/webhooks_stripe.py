from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/webhooks/stripe", tags=["webhooks"])


@router.post("")
async def stripe_webhook() -> None:
    # Stub: non funzionale. Verrà implementato nel task dedicato.
    raise HTTPException(status_code=501, detail="Not implemented")
