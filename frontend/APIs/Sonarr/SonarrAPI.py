import asyncio

from sonarr import Sonarr

API_TOKEN = None
SONARR_IP = None

class SonarrInstance():
    async def main():
        async with Sonarr() as sonarr:
            info = await sonarr.update()
            queue = await sonarr.queue()