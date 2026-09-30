import json
from urllib.parse import quote
from urllib.request import Request, urlopen


class WeatherService:
    GEOCODING_URL = (
        "https://geocoding-api.open-meteo.com/v1/search"
        "?name={city}&count=1&language=en&format=json"
    )

    WEATHER_URL = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude={latitude}"
        "&longitude={longitude}"
        "&current=temperature_2m,relative_humidity_2m,"
        "apparent_temperature,weather_code,wind_speed_10m"
        "&timezone=auto"
    )

    WEATHER_CODES = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }

    def _get_json(self, url):
        request = Request(
            url,
            headers={"User-Agent": "Skyrovix-Weather-Dashboard/1.0"}
        )

        with urlopen(request, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))

    def get_weather(self, city):
        city_query = quote(city)

        geocoding_url = self.GEOCODING_URL.format(city=city_query)
        location_data = self._get_json(geocoding_url)

        results = location_data.get("results")

        if not results:
            raise ValueError(f"City '{city}' was not found.")

        location = results[0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        weather_url = self.WEATHER_URL.format(
            latitude=latitude,
            longitude=longitude
        )

        weather_data = self._get_json(weather_url)
        current = weather_data.get("current", {})

        weather_code = current.get("weather_code")

        return {
            "city": location.get("name", city),
            "country": location.get("country", ""),
            "temperature": current.get("temperature_2m"),
            "feels_like": current.get("apparent_temperature"),
            "humidity": current.get("relative_humidity_2m"),
            "wind_speed": current.get("wind_speed_10m"),
            "condition": self.WEATHER_CODES.get(
                weather_code,
                "Unknown"
            ),
            "timezone": weather_data.get("timezone", "")
        }