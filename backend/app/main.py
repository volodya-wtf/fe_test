import uvicorn
from fastapi import FastAPI
from app.db.base import database
from app.endpoints import samples, users, auth


app = FastAPI(title="fe_samples backend")
app.include_router(samples.router, prefix="/samples", tags=["samples"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="localhost", reload=True)
