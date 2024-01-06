import time

from talon import Module, Context, actions

mod = Module()

mod.apps.sap = """
os: windows
and app.exe: Super Auto Pets.exe
"""


ctx = Context()
ctx.matches = """
app: sap
"""

@mod.action_class
class UserActions:
    def game_sap_moveto_click(x:int, y:int):
        "Moves cursor and clicks"
        actions.user.mouse_move_relative_window(x, y)
        time.sleep(0.35)
        actions.mouse_click(0)
        actions.mouse_click(0)





@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Primary attack hold"""
        actions.mouse_click(0)
        actions.mouse_drag(0)

    def noise_trigger_hiss(active: bool):
        """Primary attack hold"""
        pass
        