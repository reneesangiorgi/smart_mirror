from abc import ABC, abstractmethod

class ForRequestingWeather(ABC):
    @abstractmethod
    def get_info(self) -> str:
        # returns the outside temperature in degrees celsius
        pass


    