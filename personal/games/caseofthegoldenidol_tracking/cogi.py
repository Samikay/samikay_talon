import time

from talon import Module, Context, actions, ctrl

mod = Module()

mod.apps.cogi = """
os: windows
and title: The Case of The Golden Idol
"""


ctx = Context()
ctx.matches = """
app: cogi
"""



@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_hiss(active: bool):
        """Null out"""
        if (active):
            ctrl.mouse_click(0, up=True)
            time.sleep(0.010)
            ctrl.mouse_click(0, down=True)
            pass
        pass
        