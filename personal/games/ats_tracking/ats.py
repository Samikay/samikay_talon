import time

from talon import Module, Context, actions, ctrl

mod = Module()

mod.apps.ats = """
os: windows
and app.exe: Against the Storm.exe
"""

mod.apps.ats = """
os: windows
and title: /Slipways/i
"""

ctx = Context()
ctx.matches = """
app: ats
"""



char_pos = {}

@mod.action_class
class UserActions:
    def game_bg3_something():
        "Blah"
        actions.skip()
    


@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        actions.user.game_press_mouse(0, 0.05)

        