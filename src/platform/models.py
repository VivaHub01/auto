from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.database import Base

class Platform(Base):
    __tablename__ = 'platforms'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    organization_name: Mapped[str] = mapped_column(ForeignKey("organizations.name", ondelete="CASCADE"), nullable=False)
    
    locations = relationship("Location", back_populates="platform", cascade="all, delete-orphan")
    organization: Mapped["Organization"] = relationship("Organization", back_populates="platforms")