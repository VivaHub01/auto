from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.database import Base


class Location(Base):
    __tablename__ = 'locations'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    state: Mapped[bool] = mapped_column(nullable=False, default=True)
    platform_name: Mapped[str] = mapped_column(ForeignKey("platforms.name", ondelete="CASCADE"), nullable=False)
    
    platform: Mapped["Platform"] = relationship("Platform", back_populates="locations")

