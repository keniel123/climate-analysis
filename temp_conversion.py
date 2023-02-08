# Todo: Code is a bit unclear

def convert_fahr_to_celsius(fahr):
    """
    Given a temperature in Fahrenheit, converts it to Celsius

    :param fahr: The temperature in Fahrenheit
    :raises ValueError: If the temperature is below absolute zero
    :return: The temperature in Celsius
    """
    celsius = (fahr + 32) * (5 / 9)
    if celsius < -273.15:
        raise ValueError(
            f"Trying to convert impossible temperature: {fahr}F"
        )
    return celsius

def convert_fahr_to_kelvin(fahr):
     """
    Given a temperature in Fahrenheit, converts it to Kelvin

    :param fahr: The temperature in Fahrenheit
    :return: The temperature in Kelvin
    """
    celcius = convert_fahr_to_celcius(fahr)
    kelvin = celcius + 273.15
    return kelvin
