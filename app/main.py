from fastapi import FastAPI
from routers import movies


app = FastAPI()
app.include_router(movies)


@app.get('/')
async def index():
    return { "message":"Hello World" }
