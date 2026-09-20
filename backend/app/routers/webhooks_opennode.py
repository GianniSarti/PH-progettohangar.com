from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/webhooks/opennode", tags=["webhooks"])


@router.post("")
async def opennode_webhook() -> None:
    # Stub: provider OpenNode inattivo.
    raise HTTPException(status_code=501, detail="Not implemented")
