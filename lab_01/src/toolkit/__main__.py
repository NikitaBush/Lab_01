import argparse
import sys

from toolkit.calculator import evaluate
from toolkit.converter import convert
from toolkit.errors import ToolkitError

parser = argparse.ArgumentParser(
    prog="python -m toolkit",
    description="Калькулятор и конвертер величин",
)
commands = parser.add_subparsers(dest="command", required=True)

calc = commands.add_parser("calc", help="Посчитать выражение")
calc.add_argument("expression", help="Выражение, например: 2 + 3 * 4")

conv = commands.add_parser("convert", help="Перевести единицы")
conv.add_argument("value", type=float, help="Число")
conv.add_argument("--from", dest="from_unit", required=True, help="Из чего")
conv.add_argument("--to", dest="to_unit", required=True, help="Во что")

args = parser.parse_args()

try:
    if args.command == "calc":
        result = evaluate(args.expression)
    else:
        result = convert(args.value, args.from_unit, args.to_unit)
except ToolkitError as error:
    print("Ошибка:", error, file=sys.stderr)
    sys.exit(2)

print(result)
