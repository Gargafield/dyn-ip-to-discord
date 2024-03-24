from abc import ABC, abstractmethod

class Scraper(ABC):
    @abstractmethod
    def scrape(self) -> str:
        pass
    @abstractmethod
    def stop(self):
        pass