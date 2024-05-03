from fastapi import APIRouter, HTTPException
from database import execute_sql_query
from models.r0790888_models import Delivery
from queries.r0790888_querries import GET_ALL_DELIVERIES_QUERY, GET_DELIVERY_BY_ID_QUERY, INSERT_DELIVERY_QUERY

router = APIRouter()

@router.get("/deliveries/", response_model=list[Delivery])
async def get_all_deliveries():
    deliveries = execute_sql_query(GET_ALL_DELIVERIES_QUERY)
    if not deliveries:
        raise HTTPException(status_code=404, detail="No deliveries found")
    return deliveries

@router.get("/deliveries/{delivery_id}", response_model=Delivery)
async def get_deliveries_by_id(delivery_id: int):
    deliveries = execute_sql_query(GET_DELIVERY_BY_ID_QUERY)
    if not deliveries:
        raise HTTPException(status_code=404, detail="No deliveries found")
    return deliveries

@router.post("/deliveries/")
async def create_delivery(delivery: Delivery):
    execute_sql_query(INSERT_DELIVERY_QUERY, (delivery.delivery_id, delivery.location_name, delivery.location_address, delivery.delivery_date, delivery.product_name, delivery.product_count))
    return {"message": "Delivery created succesfully"}