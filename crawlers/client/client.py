import asyncio
import aiohttp
from typing import List

from scrapper.BaseScrapper import BaseScrapper
from utils import browser_info


class Client:
    def __init__(self, urls: List[str], scrapper: BaseScrapper):
        self.urls = urls
        self.scrapper = scrapper
        self.loop = asyncio.get_event_loop()

    async def fetch(self, url, session):
        async with session.get(url, headers={'User-Agent': browser_info}) as response:
            return await response.text()

    async def fetch_and_scrape(self, url, session):
        html = await self.fetch(url, session)
        infos = self.scrapper.scrape(html)
        return infos

    def run(self):
        return self.loop.run_until_complete(self.scrape_urls())

    async def scrape_urls(self):
        async with aiohttp.ClientSession() as session:
            return await asyncio.gather(
                *(self.fetch_and_scrape(url, session) for url in self.urls)
            )
