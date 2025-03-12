from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.database import Base
from typing import List

class Specialization(Base):
    __tablename__ = 'specializations'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    bid: Mapped[float] = mapped_column(nullable=False, default=0.00)
    classification_name: Mapped[str] = mapped_column(ForeignKey("classifications.name", ondelete="CASCADE"), nullable=False)
    
    classification: Mapped["Classification"] = relationship("Classification", back_populates="specializations")
    classification_levels: Mapped[List["ClassificationLevel"]] = relationship("ClassificationLevel", back_populates="specialization")

class ClassificationLevel(Base):
    __tablename__ = 'classification_level'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    level_name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    classification_level_rank: Mapped[int] = mapped_column(nullable=False)
    specialization_name: Mapped[str] = mapped_column(ForeignKey("specializations.name", ondelete="CASCADE"), nullable=False)
    
    specialization: Mapped["Specialization"] = relationship("Specialization", back_populates="classification_levels")