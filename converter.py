LENGTH_RATIOS = {
    'millimeter': 0.001,
    'centimeter': 0.01,
    'meter': 1.0,
    'kilometer': 1000.0,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.344
}

WEIGHT_RATIOS = {
    'milligram': 0.001,
    'gram': 1.0,
    'kilogram': 1000.0,
    'ounce': 28.349523125,
    'pound': 453.59237
}

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in LENGTH_RATIOS or to_unit not in LENGTH_RATIOS:
        raise ValueError("Invalid length unit specified.")

    return value * LENGTH_RATIOS[from_unit] / LENGTH_RATIOS[to_unit]

def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit not in WEIGHT_RATIOS or to_unit not in WEIGHT_RATIOS:
        raise ValueError("Invalid weight unit specified.")

    return value * WEIGHT_RATIOS[from_unit] / WEIGHT_RATIOS[to_unit]

def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value
    elif from_unit == "celsius":
        if to_unit == "fahrenheit": 
            return (value * 9/5) + 32
        if to_unit == "kelvin": 
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius": 
            return (value - 32) * 5/9
        if to_unit == "kelvin": 
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius": 
            return value - 273.15
        if to_unit == "fahrenheit": 
            return (value - 273.15) * 9/5 + 32
    else:
        raise ValueError("Invalid target temperature unit specified.")
