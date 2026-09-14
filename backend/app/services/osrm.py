import httpx
from typing import List, Tuple

# URL OSRM сервера (из docker-compose.yml)
OSRM_URL = "http://localhost:5000/route/v1"

async def get_route(
    start_lon: float, 
    start_lat: float, 
    end_lon: float, 
    end_lat: float
) -> dict:
    """
    Получает маршрут от OSRM
    
    Args:
        start_lon, start_lat: Координаты начала (долгота, широта)
        end_lon, end_lat: Координаты конца (долгота, широта)
    
    Returns:
        dict с маршрутом (координаты, расстояние, время)
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{OSRM_URL}/foot/{start_lon},{start_lat};{end_lon},{end_lat}",
            params={
                "overview": "full",
                "geometries": "geojson"
            }
        )
        
        if response.status_code != 200:
            raise Exception(f"OSRM error: {response.status_code}")
        
        data = response.json()
        
        if data["code"] != "Ok":
            raise Exception(f"OSRM error: {data['code']}")
        
        route = data["routes"][0]
        
        return {
            "coordinates": route["geometry"]["coordinates"],
            "distance": route["distance"],
            "duration": route["duration"]
        }
