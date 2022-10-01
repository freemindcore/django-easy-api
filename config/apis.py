from typing import Any

from asgiref.sync import sync_to_async
from django.http import HttpRequest
from ninja_jwt.authentication import JWTAuth

from easy.main import EasyAdminAPI, EasyAPI

from ninja_jwt.controller import NinjaJWTDefaultController


class EasyJWTAuth(JWTAuth):
    async def authenticate(self, request: HttpRequest, token: str) -> Any:
        return await sync_to_async(super().authenticate)(request, token)


api_v1 = EasyAPI(
    version="v1.0.0",
    easy_output=False,
)

api_admin_v1 = EasyAdminAPI(
    urls_namespace="admin_api",
    version="v1.0.0",
    auth=EasyJWTAuth(),
)

api_v1.auto_discover_controllers()
api_v1.register_controllers(NinjaJWTDefaultController)

# Automatic Admin API generation
api_admin_v1.auto_create_admin_controllers()
