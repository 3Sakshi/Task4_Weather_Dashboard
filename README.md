# Weather Dashboard
A Python-based weather dashboard that fetches live weather data using the Open-Meteo API. The project includes input validation, error handling, weather-code processing, and automated testing with pytest.

## Features
- Search weather by city name
- Fetch live weather data from an external API
- Display current temperature
- Display feels-like temperature
- Display relative humidity
- Display wind speed
- Display weather condition
- Display timezone
- City name validation
- Error handling for invalid or unavailable cities
- Automated testing using pytest

## Technologies Used
- Python
- Open-Meteo API
- urllib
- JSON
- pytest

## Project Structure
```text
Task4_Weather_Dashboard/
│
├── main.py
├── weather_service.py
├── validators.py
└── test_weather_service.py
```

## How It Works
1. The user enters a city name.
2. The application sends the city name to the Open-Meteo Geocoding API.
3. The API returns the city's latitude and longitude.
4. These coordinates are used to request current weather data.
5. The application processes the API response.
6. Weather information is displayed in a dashboard format.

## How to Run
Run the following command:
```text
python main.py
```
Enter a city name when prompted.
Example:
```text
Enter city name (or 'exit' to quit): Pune
```
The dashboard displays information such as:
```text
City        : Pune
Country     : India
Temperature : 27.9 °C
Feels Like  : 32.0 °C
Humidity    : 63 %
Wind Speed  : 1.3 km/h
Condition   : Overcast
Timezone    : Asia/Kolkata
```
The displayed weather values are obtained from the Open-Meteo API at runtime.

## Testing
Automated tests are written using pytest.
Run:
```text
pytest -q
```
Test result:
```text
3 passed
```
The tests cover:
- Successful weather-data processing
- City-not-found error handling
- Weather-code mapping

The external API is mocked during automated testing so that the tests remain independent of internet connectivity.

## Error Handling
The application handles:
- Empty city names
- Invalid city-name characters
- Cities that cannot be found
- Network/API errors
- Unexpected API responses

## Learning Outcomes
Through this project, I practiced:
- Consuming an external REST API
- Working with JSON data
- URL construction and HTTP requests
- Input validation
- Exception handling
- Python modular programming
- API response processing
- Automated testing with pytest
- GitHub project documentation

## Author
Sakshi Tayade