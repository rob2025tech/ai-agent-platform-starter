from fastapi import APIRouter

from apps.api.providers.butterbase.client import butterbase_client

router = APIRouter(
    prefix="/butterbase",
    tags=["butterbase"],
)


@router.get("/health")
async def health():
    return await butterbase_client.health()
