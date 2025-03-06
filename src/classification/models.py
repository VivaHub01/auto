from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.database import Base

class Classification(Base):
    __tablename__ = 'classifications'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    state: Mapped[bool] = mapped_column(nullable=False, default=True)
    asset_name: Mapped[str] = mapped_column(ForeignKey("assets.name", ondelete="CASCADE"), nullable=False)
    
    asset: Mapped["Asset"] = relationship("Asset", back_populates="classifications")