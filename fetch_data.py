import requests
import os
from dotenv import load_dotenv

load_dotenv()

TREFLE_API_KEY = os.getenv("TREFLE_API_KEY")

def fetch_plants_by_query(query):
    """Fetch plants based on a user query from the Trefle API."""
    TREFLE_API_ENDPOINT = f'https://trefle.io/api/v1/plants/search?token={TREFLE_API_KEY}&q={query}'
    
    try:
        response = requests.get(TREFLE_API_ENDPOINT)
        response.raise_for_status()
        data = response.json()["data"]
        return data
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []
