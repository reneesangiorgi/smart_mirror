from hexagon.ports.driving.for_requesting_traffic import ForRequestingTraffic


class FakeTrafficAdapter(ForRequestingTraffic):
    def __init__(self, minutes: int):
        super().__init__()
        self._minutes = minutes

    def get_info(self) -> str:
        return f"{self._minutes} minutes"