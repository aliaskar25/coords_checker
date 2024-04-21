from dependency_injector import containers, providers

from app.config import settings
from app.database.database import Database
from app.api_client.get_geo_data import GeoDataAPIClient
from app.repositories.geo_point_repository import GeoPointRepository
from app.services.geo_point_service import GeoPointService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    db = providers.Singleton(Database, db_url=config.DATABASE_URL)

    geo_point_repository = providers.Factory(
        GeoPointRepository, session_factory=db.provided.session
    )

    geo_point_api_client = providers.Factory(
        GeoDataAPIClient
    )

    geo_point_service = providers.Factory(
        GeoPointService,
        geo_point_repository=geo_point_repository,
        geo_data_api_client=geo_point_api_client,
    )


container = Container()
container.config.from_pydantic_settings(settings)
