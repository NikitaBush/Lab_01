from toolkit.errors import ToolkitError

OPERATORS = ["+", "-", "*", "/"]


def evaluate(text: str) -> float:
    """Главная функция: получает строку и возвращает ответ."""
    tokens = tokenize(text)
    items = validate(tokens)
    return calculate(items)


def tokenize(text: str) -> list:
    """Шаг 1. Делит строку на кусочки: "2+3.5" -> ["2", "+", "3.5"]."""
    tokens = []
    number = ""
    for char in text:
        if char in "0123456789.":
            number = number + char
        else:
            if number != "":
                tokens.append(number)
                number = ""
            if char in OPERATORS:
                tokens.append(char)
            elif char != " ":
                raise ToolkitError(f"недопустимый символ: {char}")
    if number != "":
        tokens.append(number)
    return tokens


def validate(tokens: list) -> list:
    """Шаг 2. Проверяет порядок и превращает строки в числа.

    ["2", "*", "-", "4"] -> [2.0, "*", -4.0]
    """
    if len(tokens) == 0:
        raise ToolkitError("пустое выражение")

    items = []
    i = 0
    while i < len(tokens):
        # ждём число, перед ним может стоять унарный знак
        sign = 1
        if tokens[i] == "-" or tokens[i] == "+":
            if tokens[i] == "-":
                sign = -1
            i = i + 1
        if i == len(tokens):
            raise ToolkitError("пропущено число")
        if tokens[i] in OPERATORS:
            raise ToolkitError("два оператора подряд")
        items.append(sign * to_number(tokens[i]))
        i = i + 1

        # после числа ждём оператор
        if i < len(tokens):
            if tokens[i] not in OPERATORS:
                raise ToolkitError("пропущен оператор")
            items.append(tokens[i])
            i = i + 1
            if i == len(tokens):
                raise ToolkitError("пропущено число в конце")
    return items


def calculate(items: list) -> float:
    """Шаг 3. Считает: [2.0, "+", 3.0, "*", 4.0] -> 14.0."""
    # Проход 1: сразу выполняем * и /
    rest = [items[0]]
    i = 1
    while i < len(items):
        operator = items[i]
        number = items[i + 1]
        if operator == "*":
            rest[-1] = rest[-1] * number
        elif operator == "/":
            if number == 0:
                raise ToolkitError("деление на ноль")
            rest[-1] = rest[-1] / number
        else:
            rest.append(operator)
            rest.append(number)
        i = i + 2

    # Проход 2: выполняем + и - слева направо
    result = rest[0]
    i = 1
    while i < len(rest):
        if rest[i] == "+":
            result = result + rest[i + 1]
        else:
            result = result - rest[i + 1]
        i = i + 2
    return result


def to_number(text: str) -> float:
    try:
        return float(text)
    except ValueError:
        raise ToolkitError(f"неправильное число: {text}")
