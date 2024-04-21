from sqlalchemy import exists, select, or_
from sqlalchemy.ext.asyncio import async_scoped_session


from app.database.tables.geo_point import GeoPoint
from app.schemas.geo_points import (
    RequestGeoNameModel, GeoPointModel, 
    RequestGeoLanLatModel, 
)


class GeoPointRepository:
    _model = GeoPoint

    def __init__(self, session_factory: async_scoped_session) -> None:
        self.session_factory = session_factory

    async def get_geo_point_by_display_name(
        self, request_geo_point_by_name: RequestGeoNameModel
    ) -> list[GeoPointModel]:
        async with self.session_factory() as session:
            search_terms = request_geo_point_by_name.name.split()
            query = select(self._model).where(
                or_(*[self._model.display_name.ilike(f'%{term}%') for term in search_terms])
            )

            # query = select(self._model).where(
            #     self._model.display_name.ilike(f'%{request_geo_point_by_name.name}%')
            # )
            result = await session.execute(query)
            geo_points = result.scalars().all()
            return geo_points

    async def get_geo_points_by_location(
        self, request_geo_point_by_lan_lat: RequestGeoLanLatModel
    ) -> list[GeoPointModel]:
        async with self.session_factory() as session:
            query = select(self._model).where(
                (self._model.lat == request_geo_point_by_lan_lat.lat) &
                (self._model.lon == request_geo_point_by_lan_lat.lon)
            )
            result = await session.execute(query)
            geo_points = result.scalars().all()
            return geo_points
        
    async def geo_point_exists(
        self, place_id: int
    ) -> bool:
        async with self.session_factory() as session:
            geo_point = exists().where(self._model.place_id == place_id).select()
            result = await session.execute(geo_point)
            _exists = result.scalar()
            return bool(_exists)
        
    async def create_geo_point(self, geo_point_data: GeoPointModel) -> GeoPoint:
        async with self.session_factory() as session:
            new_geo_point = self._model(
                place_id=geo_point_data.place_id,
                lat=geo_point_data.lat,
                lon=geo_point_data.lon,
                display_name=geo_point_data.display_name,
                geo_class=geo_point_data.geo_class,
                geo_type=geo_point_data.geo_type,
                importance=geo_point_data.importance
            )
            session.add(new_geo_point)
            await session.commit()
            return new_geo_point
