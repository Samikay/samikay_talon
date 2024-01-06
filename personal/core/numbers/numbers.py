from typing import Iterator, Union

from talon import Context, Module

mod = Module()
ctx = Context()

digit_list = "zero one two three four five six seven eight nine".split()

numbers9 = {name: str(i+1) for i, name in enumerate(digit_list[1:])}
mod.list("numbers9")
ctx.lists["user.numbers9"] = numbers9

@mod.capture(rule="{user.numbers9}")
def n9(m) -> int:
    "Numbers up to nine"
    return int(m["numbers9"]) if hasattr(m, "numbers9") else 1