from hexagon.ports.driving.for_requesting_traffic import ForRequestingTraffic


class RealTrafficAdapter(ForRequestingTraffic):

    def get_info(self) -> str:
        duration = self._get_trip_duration_from_google_maps_in_minutes()
        return f"{self._convert_to_minutes(duration)} minutes"

    def _get_trip_duration_from_google_maps_in_minutes(self) -> int:
        # pretend we're doing something with an outside url here
        return "1h5min"
    
    def _convert_to_minutes(self, duration: str) -> int:
        hours, minutes = 0, 0
        if 'h' in duration:
            hours_part, duration = duration.split('h')
            hours = int(hours_part)
        if 'min' in duration:
            minutes_part = duration.replace('min', '')
            minutes = int(minutes_part)
        return hours * 60 + minutes