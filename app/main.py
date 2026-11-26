from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.database import get_db
from app.redis_client import get_redis

app = FastAPI(title="КТПУ API", version="1.0.0")

@app.get("/")
async def root():
    return {"status": "ok", "message": "FastAPI is running smoothly!"}

@app.get("/check-db")
async def check_db(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        return {"db_status": "connected", "result": result.scalar()}
    except Exception as e:
        return {"db_status": "error", "message": str(e)}

@app.get("/check-redis")
async def check_redis():
    try:
        r = await get_redis()
        await r.ping()
        return {"redis_status": "connected"}
    except Exception as e:
        return {"redis_status": "error", "message": str(e)}