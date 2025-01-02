from datetime import datetime
from hexagon.ports.driven.for_requesting_weather import ForRequestingWeather
import requests


class RealWeatherAdapter(ForRequestingWeather):
    def __init__(self):
        super().__init__()

    def get_info(self) -> str:
        temperature = self._get_temperature_from_some_weather_api()
        self._celsius = self._convert_to_celsius(temperature)
        return f"{self._celsius} °C"

    def _get_temperature_from_some_weather_api(self) -> int:
        # pretend we are getting the temperature from a weather API in Fahrenheit
        response = {
            "lat": 52.2297,
            "lon": 21.0122,
            "timezone": "Europe/Warsaw",
            "timezone_offset": 3600,
            "data": [
                {
                    "dt": 1645888976,
                    "sunrise": 1645853361,
                    "sunset": 1645891727,
                    "temp": 82.13,
                    "unit": "Fahrenheit",
                    "feels_like": 276.44,
                    "pressure": 1029,
                    "humidity": 64,
                    "dew_point": 272.88,
                    "uvi": 0.06,
                    "clouds": 0,
                    "visibility": 10000,
                    "wind_speed": 3.6,
                    "wind_deg": 340,
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d",
                        }
                    ],
                }
            ],
        }
        temperature_fahrenheit = response["data"][0]["temp"]

        return temperature_fahrenheit

    def _convert_to_celsius(self, temperature: int) -> float:
        return round((temperature - 32) * 5.0 / 9.0, 1)
