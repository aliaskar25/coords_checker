from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.containers import Container
from app.schemas.geo_points import (
    RequestGeoNameModel, RequestGeoLanLatModel
)
from app.services.geo_point_service import GeoPointService


geo_point_router = APIRouter(prefix="/v1/geopoints")


@geo_point_router.post("/get-by-name")
@inject
async def get_geopoint_by_name(
    body: RequestGeoNameModel, 
    geo_point_service: GeoPointService = Depends(Provide[Container.geo_point_service]),
):
    return await geo_point_service.get_geo_by_display_name(body)



@geo_point_router.post("/get-by-lan-lat")
@inject
async def get_geopoint_by_lan_lat(
    body: RequestGeoLanLatModel, 
    geo_point_service: GeoPointService = Depends(Provide[Container.geo_point_service]),
): 
    return await geo_point_service.get_geo_by_lan_lat(body)
