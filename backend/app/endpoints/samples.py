from fastapi import APIRouter, Depends
from app.repositories.samples import SampleRepository
from app.models.samples import Sample, SampleIn, SampleStat
from .depends import get_sample_repository, get_current_user
from app.models.user import User


router = APIRouter()


@router.post("/", response_model=Sample)
async def create_sample(
    sample: SampleIn,
    samples: SampleRepository = Depends(get_sample_repository),
    current_user: User = Depends(get_current_user),
):
    return await samples.create_sample(s=sample)


@router.get("/max/{month}", response_model=SampleStat)
async def max_for_month(
    month: int,
    samples: SampleRepository = Depends(get_sample_repository),
    current_user: User = Depends(get_current_user),
):
    return await samples.max_for_month(month=month)


@router.get("/min/{month}", response_model=SampleStat)
async def min_for_month(
    month: int,
    samples: SampleRepository = Depends(get_sample_repository),
    current_user: User = Depends(get_current_user),
):
    return await samples.min_for_month(month=month)


@router.get("/avg/{month}", response_model=SampleStat)
async def avg_for_month(
    month: int,
    samples: SampleRepository = Depends(get_sample_repository),
    current_user: User = Depends(get_current_user),
):
    return await samples.avg_for_month(month=month)
