from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(
    title='NewsBotAPI',
    version='0.1.0',
    description='Newsbot API',
    debug=True,
)
app.include_router(router, prefix="/api", tags=["api"])


@app.get("/")
async def root():
    return {"message": "AI Bot API"}

