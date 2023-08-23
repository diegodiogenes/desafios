from abc import ABC, abstractmethod


class BaseScrapper(ABC):

    @abstractmethod
    def scrape(self, base_html: str):
        pass
