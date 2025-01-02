
def show_today(traffic_recipient, weather_recipient) -> str:
    info = {
        "weather": weather_recipient.get_info(),
        "traffic": traffic_recipient.get_info(),
        "news": "ajax won"
    }

    return f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Good morning, handsome one!

Today, outside temperature is {info['weather']}.
If you leave now, you will arrive in {info['traffic']}.
Also, did you know that {info['news']}?

Have a good one!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

