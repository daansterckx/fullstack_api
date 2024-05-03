from models.r0930552_models import Tour
from queries.r0930552_querries import GET_ALL_TOURS_QUERY, GET_TOUR_BY_ID_QUERY, INSERT_TOUR_QUERY
from database import execute_sql_query
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/tours/", response_model=list[Tour])
async def get_all_tours(): 
    tours = execute_sql_query(GET_ALL_TOURS_QUERY)
    if not tours:
        raise HTTPException(status_code=404, detail="No tours found")
    return tours

@router.get("/tours/{tour_id}", response_model=Tour)
async def get_tour_by_id(tour_id: int): 
    tour = execute_sql_query(GET_TOUR_BY_ID_QUERY, (tour_id,))
    if not tour:
        raise HTTPException(status_code=404, detail="No beers found")
    return tour
@router.post("/tours/")
async def create_tour(tour: Tour):
    execute_sql_query(INSERT_TOUR_QUERY, (tour.tour_id, tour.tour_name, tour.description, tour.tour_date, tour.max_attendees,))
    return {"message": "tour created successfully"}
