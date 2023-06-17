import asyncio
import requests
from aiohttp import ClientSession
from pytile import async_login

#Traccar Server (enter your Traccar Serve IP)
server_ip = "10.237.104.72"

#Tile Account Credentials (enter your Tile Account Login)
email = "johndoe@hotmail.com"
password = "secretpassword"

async def main() -> None:
    """Run!"""
    async with ClientSession() as session:
        api = await async_login(email, password, session)

        tiles = await api.async_get_tiles()
        #print(tiles)

        for tile_uuid, tile in tiles.items():
            name = tile.name
            lat = tile.latitude
            lon = tile.longitude
            alt = tile.altitude
            uuid = tile.uuid
            timestamp = tile.last_timestamp
            #print(name, lat, lon, alt, uuid, timestamp)
            print("Tile: " + name + ", Traccar device identifier/uniqueID is: ">

            url = "http://{0}:5055/?id={1}&lat={2}&lon={3}&timestamp={4}&altitu>
            server_ip,
            uuid,
            lat,
            lon,
            timestamp,
            alt
            )

            requests.put(url)

asyncio.run(main())
