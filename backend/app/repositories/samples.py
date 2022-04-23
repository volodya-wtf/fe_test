from app.db.samples import samples
from app.models.samples import Sample, SampleIn, SampleStat
from .base import BaseRepository
from sqlalchemy import func, select


class SampleRepository(BaseRepository):
    async def create_sample(self, s: SampleIn) -> Sample:
        sample = Sample(
            title=s.title, month=s.month, Fe=s.Fe, Ca=s.Ca, S=s.S, Si=s.Si, Al=s.Al
        )

        values = {**sample.dict()}
        values.pop("id", None)  # Удаление автоинкрементного поля

        query = samples.insert().values(**values)
        sample.id = await self.database.execute(query)

        return sample

    async def max_for_month(self, month: int) -> SampleStat:
        Fe_max = await self.database.execute(
            select(func.max(samples.c.Fe)).where(samples.c.month == month)
        )
        Ca_max = await self.database.execute(
            select(func.max(samples.c.Ca)).where(samples.c.month == month)
        )
        S_max = await self.database.execute(
            select(func.max(samples.c.S)).where(samples.c.month == month)
        )
        Si_max = await self.database.execute(
            select(func.max(samples.c.Si)).where(samples.c.month == month)
        )
        Al_max = await self.database.execute(
            select(func.max(samples.c.Al)).where(samples.c.month == month)
        )

        sample_max = SampleStat(Fe=Fe_max, Ca=Ca_max, S=S_max, Si=Si_max, Al=Al_max)

        return sample_max

    async def min_for_month(self, month: int) -> SampleStat:
        Fe_min = await self.database.execute(
            select(func.min(samples.c.Fe)).where(samples.c.month == month)
        )
        Ca_min = await self.database.execute(
            select(func.min(samples.c.Ca)).where(samples.c.month == month)
        )
        S_min = await self.database.execute(
            select(func.min(samples.c.S)).where(samples.c.month == month)
        )
        Si_min = await self.database.execute(
            select(func.min(samples.c.Si)).where(samples.c.month == month)
        )
        Al_min = await self.database.execute(
            select(func.min(samples.c.Al)).where(samples.c.month == month)
        )

        sample_min = SampleStat(Fe=Fe_min, Ca=Ca_min, S=S_min, Si=Si_min, Al=Al_min)

        return sample_min

    async def avg_for_month(self, month: int) -> SampleStat:
        Fe_avg = await self.database.execute(
            select(func.avg(samples.c.Fe)).where(samples.c.month == month)
        )
        Ca_avg = await self.database.execute(
            select(func.avg(samples.c.Ca)).where(samples.c.month == month)
        )
        S_avg = await self.database.execute(
            select(func.avg(samples.c.S)).where(samples.c.month == month)
        )
        Si_avg = await self.database.execute(
            select(func.avg(samples.c.Si)).where(samples.c.month == month)
        )
        Al_avg = await self.database.execute(
            select(func.avg(samples.c.Al)).where(samples.c.month == month)
        )

        sample_avg = SampleStat(Fe=Fe_avg, Ca=Ca_avg, S=S_avg, Si=Si_avg, Al=Al_avg)

        return sample_avg
