import subprocess
import sys


def run_toolkit(*arguments):
    command = [sys.executable, "-m", "toolkit", *arguments]
    return subprocess.run(command, capture_output=True, text=True, check=False)


def test_cli_success():
    result = run_toolkit("calc", "2 + 3")
    assert result.returncode == 0
    assert result.stdout.strip() == "5.0"


def test_cli_error():
    result = run_toolkit("calc", "5 / 0")
    assert result.returncode == 2
    assert result.stdout == ""
