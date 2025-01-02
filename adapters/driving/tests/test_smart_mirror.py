from adapters.driven.FakeWeatherAdapter import FakeWeatherAdapter
from hexagon.app.smart_mirror import show
from adapters.driven.FakeTrafficAdapter import FakeTrafficAdapter
import pytest


@pytest.fixture
def traffic_recipient():
    return FakeTrafficAdapter(15)

@pytest.fixture
def weather_recipient():
    return FakeWeatherAdapter(7)

def test_it_shows_traffic_info(traffic_recipient, weather_recipient):
    mirror = show(traffic_recipient, weather_recipient)
    assert "If you leave now, you will arrive in 15 minutes" in mirror

def test_it_shows_weather_info(traffic_recipient, weather_recipient):
    mirror = show(traffic_recipient, weather_recipient)
    assert "Today, outside temperature is 7 °C" in mirror


def test_it_shows_news_info(traffic_recipient, weather_recipient):
    mirror = show(traffic_recipient, weather_recipient)
    assert "did you know that ajax won" in mirror
    
    