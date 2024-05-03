from fastapi import FastAPI
from routes.r0931795_endpoints import router as beer_router
from routes.r0930552_endpoints import router as tour_router

app = FastAPI()

app.include_router(beer_router)
app.include_router(tour_router)
