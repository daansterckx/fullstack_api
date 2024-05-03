from fastapi import APIRouter, HTTPException
from database import execute_sql_query
from models.r0931795_models import Beer
from queries.r0931795_queries import GET_ALL_BEERS_QUERY, GET_BEER_BY_ID_QUERY, INSERT_BEER_QUERY

router = APIRouter()

@router.get("/beers/", response_model=list[Beer])
async def get_all_beers():
    beers = execute_sql_query(GET_ALL_BEERS_QUERY)
    if not beers:
        raise HTTPException(status_code=404, detail="No beers found")
    return beers

@router.get("/beers/{beer_id}", response_model=Beer)
async def get_beer_by_id(beer_id: int):
    beer = execute_sql_query(GET_BEER_BY_ID_QUERY, (beer_id,))
    if not beer:
        raise HTTPException(status_code=404, detail="Beer not found")
    return beer[0]

@router.post("/beers/")
async def create_beer(beer: Beer):
    execute_sql_query(INSERT_BEER_QUERY, (beer.name, beer.price))
    return {"message": "Beer created successfully"}
