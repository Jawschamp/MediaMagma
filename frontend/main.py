from APIs.Sonarr.SonarrAPI import SonarrInstance

import asyncio

if __name__ == "__main__":
    loop = asyncio.get_evet_loop(SonarrInstance.main())
    loop.run_until_complete()