from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.database import Base

class Asset(Base):
    __tablename__ = 'assets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    state: Mapped[bool] = mapped_column(nullable=False, default=True)
    location_name: Mapped[str] = mapped_column(ForeignKey("locations.name", ondelete="CASCADE"), nullable=False)
    
    location: Mapped["Location"] = relationship("Location", back_populates="assets")
    classifications = relationship("Classification", back_populates="asset", cascade="all, delete-orphan")