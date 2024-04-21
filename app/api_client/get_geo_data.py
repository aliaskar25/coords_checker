import aiohttp

from app.config import API_CLIENT_KEY


class GeoDataAPIClient:
    API_KEY = API_CLIENT_KEY
    FORWARD_GEOCODE_URL = "https://geocode.maps.co/search?q={}&api_key={}"
    REVERSE_GEOCODE_URL = "https://geocode.maps.co/reverse?lat={}&lon={}&api_key={}"

    async def fetch_data(self, session, url: str):
        async with session.get(url) as response:
            return await response.json()

    async def fetch_forward_geocode(self, address: str):
        request_url = self.FORWARD_GEOCODE_URL.format(address, self.API_KEY)
        async with aiohttp.ClientSession() as session:
            res = await self.fetch_data(session, request_url)
        return res

    async def fetch_reverse_forward_geocode(self, lat: str, lon: str):
        request_url = self.REVERSE_GEOCODE_URL.format(lat, lon, self.API_KEY)
        async with aiohttp.ClientSession() as session:
            res = await self.fetch_data(session, request_url)
        return res 
