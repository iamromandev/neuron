from fastapi import APIRouter

from .agent import router as _agent_router

_subrouters = [
    _agent_router,
]

router = APIRouter(prefix="/agent", tags=["Agent"])

for subrouter in _subrouters:
    router.include_router(subrouter)
