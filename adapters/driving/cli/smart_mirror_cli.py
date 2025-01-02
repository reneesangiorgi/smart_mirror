from adapters.driven.RealWeatherAdapter import RealWeatherAdapter
from adapters.driven.RealTrafficAdapter import RealTrafficAdapter
import click
from hexagon.app.smart_mirror import show

@click.command()
def show_mirror():
    traffic_recipient = RealTrafficAdapter()
    weather_recipient = RealWeatherAdapter()
    info = show(traffic_recipient, weather_recipient)
    click.echo(info)


if __name__ == '__main__':
    show_mirror()