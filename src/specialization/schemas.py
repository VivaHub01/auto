from pydantic import BaseModel, Field
from enum import Enum
from typing import List

class LevelName(str, Enum):
    CAT1 = '1CAT'
    CAT2 = '2CAT'
    CAT3 = '3CAT'
    CAT4 = '4CAT'
    CAT5 = '5CAT'
    CAT6 = '6CAT'
    CAT7 = '7CAT'

class Description(str, Enum):
    CAT1 = '1 разряд'
    CAT2 = '2 разряд'
    CAT3 = '3 разряд'
    CAT4 = '4 разряд'
    CAT5 = '5 разряд'
    CAT6 = '6 разряд'
    CAT7 = '7 разряд'

class ClassificationLevelRank(int, Enum):
    RANK1 = 1
    RANK2 = 2
    RANK3 = 3
    RANK4 = 4
    RANK5 = 5
    RANK6 = 6
    RANK7 = 7

class SpecializationIn(BaseModel):
    name: str
    description: str | None = None
    bid: float = Field(ge=0.0, default=0.0)
    classification_name: str

class SpecializationOut(BaseModel):
    name: str
    description: str | None = None
    bid: float
    classification_name: str

class ClassificationLevelIn(BaseModel):
    level_name: LevelName
    description: Description
    classification_level_rank: ClassificationLevelRank
    specialization_name: str

class ClassificationLevelOut(BaseModel):
    level_name: LevelName
    description: Description
    classification_level_rank: ClassificationLevelRank
    specialization_name: str

class ClassificationLevelWithSpecializationOut(BaseModel):
    id: int
    level_name: LevelName
    description: Description | None = None
    classification_level_rank: ClassificationLevelRank
    specialization: SpecializationOut

class SpecializationWithClassificationLevelsOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    bid: float
    classification_name: str
    classification_levels: List[ClassificationLevelOut]