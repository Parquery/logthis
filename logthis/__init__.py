#!/usr/bin/env python3
"""
Provide singleton, two-level, colorful, thread-safe, knob-free, logging for in-house software.

"""
import datetime
import inspect
import os
import sys
import threading
from typing import Tuple  # pylint: disable=unused-import


class State:
    """Represent the global logging state."""

    lock = threading.Lock()
    stdout = sys.stdout
    stderr = sys.stderr


class Colors:
    """List the terminal colours."""

    kConsoleDefault = "\033[0m"
    kForeBlack = "\033[30m"
    kForeBlue = "\033[34m"
    kForeRed = "\033[31m"
    kForeMagenta = "\033[35m"
    kForeGreen = "\033[32m"
    kForeCyan = "\033[36m"
    kForeYellow = "\033[33m"
    kForeWhite = "\033[37m"
    kForeConsole = "\033[39m"

    kForelightBlack = "\033[90m"
    kForelightBlue = "\033[94m"
    kForelightRed = "\033[91m"
    kForelightMagenta = "\033[95m"
    kForelightGreen = "\033[92m"
    kForelightCyan = "\033[96m"
    kForelightYellow = "\033[93m"
    kForelightWhite = "\033[97m"

    kBackBlack = "\033[40m"
    kBackBlue = "\033[44m"
    kBackRed = "\033[41m"
    kBackMagenta = "\033[45m"
    kBackGreen = "\033[42m"
    kBackCyan = "\033[46m"
    kBackYellow = "\033[43m"
    kBackWhite = "\033[47m"
    kBackConsole = "\033[49m"

    kBacklightBlack = "\033[100m"
    kBacklightBlue = "\033[104m"
    kBacklightRed = "\033[101m"
    kBacklightMagenta = "\033[105m"
    kBacklightGreen = "\033[102m"
    kBacklightCyan = "\033[106m"
    kBacklightYellow = "\033[103m"
    kBacklightWhite = "\033[107m"


def filename_line(skip: int = 2) -> Tuple[str, int]:
    """
    Extract the module file name and line by inspection.

    :param skip: the depth of the calling function in the stack trace
    :return: file name and the line number

    """
    stack = inspect.stack()
    start = skip
    parentframe = stack[start][0]

    filename = 'N/A'
    module = inspect.getmodule(parentframe)
    if module:
        filename = os.path.basename(os.path.realpath(module.__file__))

    return filename, parentframe.f_lineno


def say(message: str) -> None:
    """
    Print a formatted log message to STDOUT and flush.

    :param message: to be displayed

    """
    with State.lock:
        filename, line = filename_line()
        State.stdout.write(say_as_text(filename=filename, line=line, message=message))
        State.stdout.flush()


def say_as_text(filename: str, line: int, message: str) -> str:
    """
    Generate 'say' message as a string.

    :param filename: path to the script, usually you want to pass __file__
    :param line: line number in the script, usually you want to pass inspect.currentframe().f_lineno
    :param message: to be displayed
    :return: whole formatted message which the 'say' function will display

    """
    return "{blue}{fname}: {line:5d}: {dt}:{endcolor} {msg}\n".format(
        blue=Colors.kForeBlue,
        fname=filename,
        line=line,
        dt=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ"),
        msg=message,
        endcolor=Colors.kConsoleDefault)


def err(message: str) -> None:
    """
    Print a formatted log message to STDERR and flush.

    :param message: to be displayed

    """
    filename, line = filename_line()

    with State.lock:
        State.stderr.write(err_as_text(filename=filename, line=line, message=message))
        State.stderr.flush()


def err_as_text(filename: str, line: int, message: str) -> str:
    """
    Generate 'err' message as a string.

    :param filename: path to the script, usually you want to pass __file__
    :param line: line number in the script, usually you want to pass inspect.currentframe().f_lineno
    :param message: to be displayed
    :return: whole formatted message which the 'err' function will display

    """
    return "{red}{fname}: {line:5d}: {dt}:{endcolor} {msg}\n".format(
        red=Colors.kForeRed,
        fname=filename,
        line=line,
        dt=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ"),
        msg=message,
        endcolor=Colors.kConsoleDefault)
