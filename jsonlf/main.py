#!/usr/bin/env python3

import json
import re
import sys

from pygments import formatters, highlight, lexers, style, token
from pygments.styles import get_all_styles, get_style_by_name
from pygments.util import ClassNotFound


def gen_tb_style(base_style):
    class CustomTracebackStyle(style.Style):
        base = "#FF0000"
        styles = {
            **base_style.styles,
            token.Token: f"{base}",
        }

    return CustomTracebackStyle


def readall(style=None):
    is_traceback = False
    tb_style = gen_tb_style(style or get_style_by_name("default"))
    for line in sys.stdin:
        try:
            line = json.loads(line)
            line = json.dumps(line, indent=4, sort_keys=True)
            is_traceback = False
            line = highlight(line, lexers.JsonLexer(), formatters.Terminal256Formatter(style=style))
        except:
            pass

        def traceback_highlight() -> str:
            return highlight(
                line,
                lexers.PythonTracebackLexer(),
                formatters.Terminal256Formatter(style=tb_style),
            )

        if is_traceback:
            if not re.match(r"^\s+", line):
                is_traceback = False
            line = traceback_highlight()

        elif line.startswith("Traceback"):
            is_traceback = True
            line = traceback_highlight()

        line = line.replace("\\n", "\n")
        print(line, end="")


def main():
    if len(sys.argv) > 1:
        try:
            chosen_style = get_style_by_name(sys.argv[1])
        except (ImportError, ClassNotFound):
            print(f"chosen_style {sys.argv[1]} not found")
            print("Available styles:")
            for chosen_style in get_all_styles():
                print(f"  {chosen_style}")
            sys.exit(1)
    else:
        chosen_style = None
    readall(chosen_style)
