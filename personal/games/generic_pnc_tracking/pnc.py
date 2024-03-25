import time

from talon import Module, Context, actions, ctrl
from .._handy.input_holder import InputHolder

mod = Module()


mod.apps.generic_pnc = """
os: windows
and title: /Chants of Sennaar/i
"""

mod.apps.generic_pnc = """
os: windows
and title: /Slipways/i
"""

mod.apps.generic_pnc = """
os: windows
and title: /LostInPlay/i
"""

mod.apps.generic_pnc = """
os: windows
and app.exe: LostInPlay.exe
"""


mod.apps.generic_pnc = """
os: windows
and title: /Backpack Battles/i
"""

mod.apps.generic_pnc = """
os: windows
and title: /Curious Expedition/i
"""

mod.apps.generic_pnc = """
os: windows
and app.exe: sliceanddice.exe
"""

mod.apps.generic_pnc = """
os: windows
and app.exe: tangle tower.exe
"""

mod.apps.generic_pnc = """
os: windows
and app.exe: Dorfromantik.exe
"""

ctx = Context()
ctx.matches = """
app: generic_pnc
"""

inputHolder = InputHolder()

@ctx.action_class("user")
class OverrideActions:
    def noise_pop():
        #ctrl.mouse_click(0, down=True)
        #time.sleep(0.05)
        #ctrl.mouse_click(0, up=True)
        ctrl.mouse_click(0)
        inputHolder.resetClick()


    def noise_trigger_hiss(active: bool):
        if (active):
          #actions.user.game_mouse_drag(0)
          #actions.user.game_mouse_doubleclick(0)
          #  actions.user.game_ double_click()
          #inputHolder.hold_click(2)
          inputHolder.hold_click(0)
          pass
        else: 
          pass
          
        

    def noise_trigger_shush(active: bool):
        if (active):
          #actions.tracking.control_gaze_toggle(False)
          #actions.user.game_mouse_doubleclick(0)
          #  actions.user.game_ double_click()
          #inputHolder.hold_click(2)
          actions.user.game_press_mouse(1, 0.05)
          pass
        else: 
          #actions.tracking.control_gaze_toggle(True)
          #actions.user.mouse_drag_end()
          pass
      
  