from fastapi import APIRouter

from app.routers.v1.geo_point import geo_point_router

router = APIRouter(tags=["API"], prefix="/api")

router.include_router(geo_point_router, tags=["geopoints"])
