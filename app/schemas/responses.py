from pydantic import BaseModel

from .geo_points import GeoPointModel


class GeoPointsListResponse(BaseModel):
    geo_points: list[GeoPointModel]
