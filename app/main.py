from fastapi import FastAPI
from app.api import auth_api, tenders_api, submissions_api, match_api
from app.db import engine, Base
import asyncio

app = FastAPI(title="ProcureLink Hub API")

# include routers
app.include_router(auth_api.router)
app.include_router(tenders_api.router)
app.include_router(submissions_api.router)
app.include_router(match_api.router)

# create tables at startup (for dev)
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
