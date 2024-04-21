from pydantic import BaseModel


class RequestGeoNameModel(BaseModel):
    name: str


class RequestGeoLanLatModel(BaseModel):
    lon: str
    lat: str


class GeoPointModel(BaseModel):
    place_id: int
    lat: str
    lon: str
    display_name: str
    geo_class: str | None
    geo_type: str | None
    importance: float | None

    class Config:
        orm_mode = True

