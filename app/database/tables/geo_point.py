from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.database.tables.base import Base


class GeoPoint(Base):
    __tablename__ = "geo_point"

    id: Mapped[int] = mapped_column(primary_key=True)
    place_id: Mapped[int] = mapped_column(Integer, unique=True)
    lat: Mapped[str] = mapped_column(String(255))
    lon: Mapped[str] = mapped_column(String(255))
    display_name: Mapped[str] = mapped_column(String(1024))
    geo_class: Mapped[str | None] = mapped_column(String(64))
    geo_type: Mapped[str | None] = mapped_column(String(64))
    importance: Mapped[float | None] = mapped_column(Float)
