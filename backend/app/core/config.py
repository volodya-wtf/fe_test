from email.policy import default
from starlette.config import Config


config = Config(".env")

ALGORITHM = config("ALGORITHM")
SECRET_KEY = config("SECRET_KEY", cast=str, default="default secret key")

PG_PASSWORD = config("PG_PASSWORD")
PG_USERNAME = config("PG_USERNAME")
PG_DATABASE = config("PG_DATABASE")
PG_HOST = config("PG_HOST")
print(PG_HOST)
PG_PORT = config("PG_PORT")


DATABASE_URL = (
    f"postgresql://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"
)

ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES")
