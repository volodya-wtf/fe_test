from starlette.config import Config

config = Config(".env")

SECRET_KEY = config("SECRET_KEY", cast=str, default="default secret key")
