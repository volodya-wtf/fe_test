import sqlalchemy
from .base import metadata
import datetime


samples = sqlalchemy.Table(
    "samples",
    metadata,
    sqlalchemy.Column(
        "id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True
    ),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("month", sqlalchemy.Integer),
    sqlalchemy.Column("Fe", sqlalchemy.Numeric(10, 2)),
    sqlalchemy.Column("Ca", sqlalchemy.Numeric(10, 2)),
    sqlalchemy.Column("S", sqlalchemy.Numeric(10, 2)),
    sqlalchemy.Column("Si", sqlalchemy.Numeric(10, 2)),
    sqlalchemy.Column("Al", sqlalchemy.Numeric(10, 2)),
)
