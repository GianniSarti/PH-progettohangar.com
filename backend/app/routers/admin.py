from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("")
async def admin_root() -> None:
    # Stub: non funzionale. Nessun contenuto e nessuna autenticazione ancora
    # implementata: l'autenticazione va definita prima di aggiungere qualsiasi
    # endpoint reale sotto /admin.
    raise HTTPException(status_code=501, detail="Not implemented")
