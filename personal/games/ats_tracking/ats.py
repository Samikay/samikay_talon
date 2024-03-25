import time

from talon import Module, Context, actions, ctrl

mod = Module()

mod.apps.ats = """
os: windows
and app.exe: Against the Storm.exe
"""

mod.apps.ats = """
os: windows
and title: /dotAge/i
"""

ctx = Context()
ctx.matches = """
app: ats
"""



char_pos = {}

@mod.action_class
class UserActions:
    def game_ats_something():
        "Blah"
        actions.skip()
    


@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_shush(active: bool):
        if (active):
            ctrl.mouse_click(1, down=True)
        else:
            ctrl.mouse_click(1, up=True)


        