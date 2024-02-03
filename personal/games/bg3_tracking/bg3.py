import time

from talon import Module, Context, actions, ctrl

mod = Module()

# This didn't work...
mod.apps.baldursgate3 = """
os: windows
and app.exe: bg3.exe
"""

# this didn't work
mod.apps.baldursgate3 = """
os: windows
and app.exe: LariLauncher.exe
"""

# Used 'print title' and copied it directly. This works.
mod.apps.baldursgate3 = """
os: windows
and title: Baldur's Gate 3 (2560x1440) - (DX11) - (6 + 6 WT)
"""

mod.apps.baldursgate3 = """
os: windows
and title: Baldur's Gate 3 (1920x1080) - (DX11) - (6 + 6 WT)
"""

ctx = Context()
ctx.matches = """
app: baldursgate3
"""


@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_hiss(active: bool):
        """Null out"""
        pass
        