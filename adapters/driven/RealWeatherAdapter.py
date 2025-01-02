from hexagon.ports.driving.for_requesting_weather import ForRequestingWeather


class RealWeatherAdapter(ForRequestingWeather):
    def __init__(self):
        super().__init__()

    def get_info(self) -> str:
        # pretend we are getting the temperature from a weather API in Fahrenheit
        temperature = self._get_temperature_from_some_weather_api()
        self._celsius = self._convert_to_celsius(temperature)
        return f"{self._celsius} °C"
    
    def _get_temperature_from_some_weather_api(self) -> int:
        return 101
    
    def _convert_to_celsius(self, temperature: int) -> int:
        return round((temperature - 32) * 5.0/9.0, 1)