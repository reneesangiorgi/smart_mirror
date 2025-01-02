from abc import ABC, abstractmethod

class ForRequestingTraffic(ABC):
    @abstractmethod
    def get_info(self) -> str:
        # returns the duration of the trip in minutes
        pass


    