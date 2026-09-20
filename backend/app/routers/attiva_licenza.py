from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/attiva-licenza", tags=["licenze"])


@router.post("")
async def attiva_licenza() -> None:
    # Stub: non funzionale.
    raise HTTPException(status_code=501, detail="Not implemented")
