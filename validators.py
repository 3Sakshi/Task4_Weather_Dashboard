def validate_city(city):
    if not city or not city.strip():
        raise ValueError("City name cannot be empty.")

    city = city.strip()

    if not all(char.isalpha() or char.isspace() or char in "-'" for char in city):
        raise ValueError(
            "City name can contain only letters, spaces, hyphens, and apostrophes."
        )

    return city


def validate_temperature(temperature):
    if not isinstance(temperature, (int, float)):
        raise ValueError("Temperature must be a number.")

    if temperature < -100 or temperature > 100:
        raise ValueError("Temperature must be between -100 and 100 °C.")

    return temperature