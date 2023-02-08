# Todo: Code is a bit unclear

def convert_fahr_to_celcius(fahr):
    celcius = (fahr - 32) * (5 / 9)
    return celcius

def convert_fahr_to_kelvin(fahr):
    celcius = convert_fahr_to_celcius(fahr)
    kelvin = celcius + 273.15
    return kelvin
