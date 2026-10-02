from toolkit.errors import ToolkitError

LENGTH = {"mm": 1, "cm": 10, "m": 1000, "km": 1000000}  # в миллиметрах
MASS = {"g": 1, "kg": 1000}  # в граммах
TEMPERATURE = ["c", "f", "k"]


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Переводит value из from_unit в to_unit."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if not is_known(from_unit):
        raise ToolkitError(f"неизвестная единица: {from_unit}")
    if not is_known(to_unit):
        raise ToolkitError(f"неизвестная единица: {to_unit}")

    if from_unit in LENGTH and to_unit in LENGTH:
        return value * LENGTH[from_unit] / LENGTH[to_unit]
    if from_unit in MASS and to_unit in MASS:
        return value * MASS[from_unit] / MASS[to_unit]
    if from_unit in TEMPERATURE and to_unit in TEMPERATURE:
        return convert_temperature(value, from_unit, to_unit)

    raise ToolkitError(f"нельзя перевести {from_unit} в {to_unit}")


def is_known(unit: str) -> bool:
    return unit in LENGTH or unit in MASS or unit in TEMPERATURE


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    # сначала переводим в градусы Цельсия
    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if celsius < -273.15:
        raise ToolkitError("температура ниже абсолютного нуля")

    # потом из Цельсия в нужную единицу
    if to_unit == "c":
        return float(celsius)
    if to_unit == "f":
        return celsius * 9 / 5 + 32
    return celsius + 273.15
