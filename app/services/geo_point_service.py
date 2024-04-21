from app.api_client.get_geo_data import GeoDataAPIClient
from app.repositories.geo_point_repository import GeoPointRepository
from app.schemas.geo_points import (
    RequestGeoNameModel, RequestGeoLanLatModel, 
    GeoPointModel, 
)
from app.schemas.responses import (
    GeoPointsListResponse, 
)


class GeoPointService:
    def __init__(
        self,
        *,
        geo_point_repository: GeoPointRepository,
        geo_data_api_client: GeoDataAPIClient
    ) -> None:
        self._geo_point_repository = geo_point_repository
        self._geo_data_api_client = geo_data_api_client  

    async def get_geo_by_display_name(
        self, request_geo_point_by_name: RequestGeoNameModel
    ) -> GeoPointsListResponse:
        geo_points = await self._geo_point_repository.get_geo_point_by_display_name(
            request_geo_point_by_name
        )
        if not geo_points:
            geo_points = GeoPointsListResponse(geo_points=[])
            geo_points_data = await self._geo_data_api_client.fetch_forward_geocode(request_geo_point_by_name.name)
            for geo in geo_points_data:
                if await self._geo_point_repository.geo_point_exists(geo['place_id']):
                    continue
                geo_point = await self._geo_point_repository.create_geo_point(GeoPointModel(
                    place_id=geo['place_id'],
                    lat=geo['lat'],
                    lon=geo['lon'],
                    display_name=geo['display_name'],
                    geo_class=geo['class'],
                    geo_type=geo['type'],
                    importance=geo['importance']
                ))
                geo_points.geo_points.append(geo_point)
        return geo_points
    
    async def get_geo_by_lan_lat(
        self, request_geo_point_by_lan_lat: RequestGeoLanLatModel
    ) -> GeoPointsListResponse:
        geo_points = await self._geo_point_repository.get_geo_points_by_location(
            request_geo_point_by_lan_lat
        )
        if not geo_points:
            geo_points = GeoPointsListResponse(geo_points=[])
            geo_points_data = await self._geo_data_api_client.fetch_reverse_forward_geocode(
                request_geo_point_by_lan_lat.lat, request_geo_point_by_lan_lat.lon
            )   

            geo_point = await self._geo_point_repository.create_geo_point(GeoPointModel(
                place_id=geo_points_data['place_id'],
                lat=geo_points_data['lat'],
                lon=geo_points_data['lon'],
                display_name=geo_points_data['display_name'],
                geo_class=None,
                geo_type=None,
                importance=None
            ))
            geo_points.geo_points.append(geo_point)
        return geo_points 
