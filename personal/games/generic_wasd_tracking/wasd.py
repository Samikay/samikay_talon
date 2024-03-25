import time

from talon import Module, Context, actions, ctrl, cron
from .._handy.input_holder import InputHolder
from .._handy.mouse_region_handler import MouseRegionHandler

mod = Module()

mod.apps.generic_wasd = """
os: windows
and title: Thronefall
"""


ctx = Context()
ctx.matches = """
app: generic_wasd
"""

inputHolder = InputHolder()
regionHandler = MouseRegionHandler()

@mod.action_class
class UserActions:
    def game_wasd_move_to_cursor(active: bool):
        "If game doesn't have some move to cursor ability, this is a viable alternative"
        if (regionHandler.has_setup() == False): 
          regionHandler.setup()
        if (active): 
          move_continuous()
          stop_move_debounce(False)
        else:
          stop_move_debounce(True)



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
          #inputHolder.hold_key("shift")
          actions.user.game_press_key("tab")
          pass
        else: 
          pass
          
    def noise_trigger_tut():
      actions.user.game_press_key("space")
        

    def noise_trigger_shush(active: bool):
        if (active):
          #actions.tracking.control_gaze_toggle(False)
          #actions.user.game_mouse_doubleclick(0)
          #inputHolder.hold_click(2)
          actions.user.mouse_drag(1)
          #actions.user.game_wasd_move_to_cursor(True)
          pass
        else: 
          #actions.user.game_wasd_move_to_cursor(False)
          #actions.tracking.control_gaze_toggle(True)
          actions.user.mouse_drag_end()
          pass
      

#
# Move job handling
#
move_job = None
last_held_keys = ""
def move_continuous():
    global move_job 
    if move_job is None:  
        move_job = cron.interval("25ms", move_continuous_helper)
        


stop_job = None
def stop_move_debounce(start: bool):
    global stop_job
    if start and stop_job == None:
        stop_job = cron.after("50ms", lambda: stop_move())
    elif not start and stop_job is not None:
        cron.cancel(stop_job)
        stop_job = None



def stop_move():
    global move_job, last_held_keys
    if move_job:
        cron.cancel(move_job)
        move_job = None
        last_held_keys = ""
        actions.user.game_keys_down_and_up(last_held_keys, "wasd")

def move_continuous_helper():
    global move_job, last_held_keys
    if move_job:
        keys = regionHandler.which_inclusive()
        if (keys != last_held_keys):
          print(keys)
          actions.user.game_keys_down_and_up(keys, "wasd")
          last_held_keys = keys

        