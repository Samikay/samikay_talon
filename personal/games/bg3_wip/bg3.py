import time

from talon import Module, Context, actions, ctrl

mod = Module()

mod.apps.baldursgate3 = """
os: windows
and app.exe: bg3.exe
"""

mod.apps.baldursgate3 = """
os: windows
and app.exe: LariLauncher.exe
"""

mod.apps.baldursgate3 = """
os: windows
and title: Baldur's Gate 3 (2560x1440) - (DX11) - (6 + 6 WT)
"""


ctx = Context()
ctx.matches = """
app: baldursgate3
"""

char_pos = {}

@mod.action_class
class UserActions:
    def game_bg3_something():
        "Blah"
        actions.skip()
    


@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_hiss(active: bool):
        """Null out"""
        pass
        