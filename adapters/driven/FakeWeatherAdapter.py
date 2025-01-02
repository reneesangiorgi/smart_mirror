from hexagon.ports.driving.for_requesting_weather import ForRequestingWeather


class FakeWeatherAdapter(ForRequestingWeather):
    def __init__(self, celsius: int):
        super().__init__()
        self._celsius = celsius

    def get_info(self) -> str:
        return f"{self._celsius} °C"