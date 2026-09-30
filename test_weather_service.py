from weather_service import WeatherService


def test_get_weather(monkeypatch):
    service = WeatherService()

    geocoding_response = {
        "results": [
            {
                "name": "Pune",
                "country": "India",
                "latitude": 18.5204,
                "longitude": 73.8567
            }
        ]
    }

    weather_response = {
        "current": {
            "temperature_2m": 28.5,
            "relative_humidity_2m": 65,
            "apparent_temperature": 30.0,
            "weather_code": 1,
            "wind_speed_10m": 12.4
        },
        "timezone": "Asia/Kolkata"
    }

    responses = [geocoding_response, weather_response]

    def mock_get_json(url):
        return responses.pop(0)

    monkeypatch.setattr(service, "_get_json", mock_get_json)

    result = service.get_weather("Pune")

    assert result["city"] == "Pune"
    assert result["country"] == "India"
    assert result["temperature"] == 28.5
    assert result["feels_like"] == 30.0
    assert result["humidity"] == 65
    assert result["wind_speed"] == 12.4
    assert result["condition"] == "Mainly clear"
    assert result["timezone"] == "Asia/Kolkata"


def test_city_not_found(monkeypatch):
    service = WeatherService()

    def mock_get_json(url):
        return {}

    monkeypatch.setattr(service, "_get_json", mock_get_json)

    try:
        service.get_weather("UnknownCity")
        assert False
    except ValueError as error:
        assert str(error) == "City 'UnknownCity' was not found."


def test_weather_code_mapping():
    service = WeatherService()

    assert service.WEATHER_CODES[0] == "Clear sky"
    assert service.WEATHER_CODES[61] == "Slight rain"
    assert service.WEATHER_CODES[95] == "Thunderstorm"