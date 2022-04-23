from typing import Optional
from pydantic import BaseModel, validator


# Модель для отображения проб
class Sample(BaseModel):
    id: Optional[str] = None

    title: str
    month: int

    Fe: float
    Ca: float
    S: float
    Si: float
    Al: float


# Модель для добавления проб
class SampleIn(BaseModel):
    title: str
    month: int

    Fe: float
    Ca: float
    S: float
    Si: float
    Al: float

    @validator("month")
    def valid_month_number(cls, v):
        if v < 1 or v > 12:
            raise ValueError("Invalid month value")
        return v


# Модель для отображения статистики
class SampleStat(BaseModel):
    Fe: float
    Ca: float
    S: float
    Si: float
    Al: float
