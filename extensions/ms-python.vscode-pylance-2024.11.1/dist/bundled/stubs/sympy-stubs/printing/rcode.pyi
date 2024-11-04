from typing import Any

from sympy.printing.codeprinter import CodePrinter

known_functions = ...
reserved_words = ...

class RCodePrinter(CodePrinter):
    printmethod = ...
    language = ...
    _default_settings: dict[str, Any] = ...
    _operators = ...
    _relationals: dict[str, str] = ...
    def __init__(self, settings=...) -> None: ...
    def indent_code(self, code) -> str | list[Any]: ...

def rcode(expr, assign_to=..., **settings) -> str | tuple[set[tuple[Any, str]], set[Any], str]: ...
def print_rcode(expr, **settings) -> None: ...