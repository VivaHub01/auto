from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.database import Base

class Organization(Base):
    __tablename__ = 'organizations'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)

    platforms = relationship("Platform", back_populates="organization", cascade="all, delete-orphan")