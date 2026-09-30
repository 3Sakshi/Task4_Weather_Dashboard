from weather_service import WeatherService
from validators import validate_city


def display_weather(weather):
    print("\n" + "=" * 45)
    print("          WEATHER DASHBOARD")
    print("=" * 45)

    print(f"City        : {weather['city']}")
    print(f"Country     : {weather['country']}")
    print(f"Temperature : {weather['temperature']} °C")
    print(f"Feels Like  : {weather['feels_like']} °C")
    print(f"Humidity    : {weather['humidity']} %")
    print(f"Wind Speed  : {weather['wind_speed']} km/h")
    print(f"Condition   : {weather['condition']}")
    print(f"Timezone    : {weather['timezone']}")

    print("=" * 45)


def main():
    service = WeatherService()

    print("\n======================================")
    print("       Python Weather Dashboard")
    print("======================================")

    while True:
        try:
            city = validate_city(
                input("\nEnter city name (or 'exit' to quit): ")
            )

            if city.lower() == "exit":
                print("\nThank you for using Weather Dashboard.")
                break

            print("\nFetching weather data...")

            weather = service.get_weather(city)
            display_weather(weather)

        except ValueError as error:
            print(f"Error: {error}")

        except Exception as error:
            print(
                "Unable to fetch weather data. "
                "Please check your internet connection and try again."
            )
            print(f"Details: {error}")


if __name__ == "__main__":
    main()