import os
import time

from talon import Context, Module, actions, app, clip, cron, ctrl, imgui, ui
from talon_plugins import eye_zoom_mouse

self = actions.self

mod = Module()

setting_mouse_move_amount = mod.setting(
    "mouse_move_amount",
    type=int,
    default=40,
    desc="The amount to move the mouse",
)

ctx = Context()

my_pop_click = True

@mod.action_class
class Actions:
  def toggle_speech():
    """enables discord (via api) and disables talon and vice versa - hook up to a foot switch press for maximum ease of use"""
    # Follow the steps in apps/discord/discord_api , you can use localhost (https://127.0.0.1) as the redirect URI.
    if actions.speech.enabled():
      actions.speech.disable()
      #actions.user.microphone_select(1) # Optional, selects 'none' microphone (so you can't make noises/'talon wake' commands) if you REALLY want to mute.
      actions.user.discord_set_mute_status(False)
    else:
      actions.speech.enable()
      #actions.user.microphone_select(2) # Reselects system default microphone
      actions.user.discord_set_mute_status(True)

  def toggle_pop_click():
    "Toggles pop_click"
    global my_pop_click
    my_pop_click = not my_pop_click


@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Click"""
        global my_pop_click
        if (my_pop_click):
          if (actions.tracking.control_zoom_enabled()):
            actions.skip()
          else:
            print("-- general_trigger pop")
            actions.mouse_click(0)

    def noise_trigger_talon_pop():
      """The default Talon pop works much better while other noises are happening"""
      global my_pop_click
      if (not my_pop_click):
        print("-- general_ <<talon>> pop")
        actions.mouse_click(0)

    # Used by the community/mouse for scrolling. Don't override here.
    #def noise_trigger_hiss(active: bool):
    #  pass

    #----
    # These need parrot (talon beta).
    #----
    # For reading tooltips more easily.
    def noise_trigger_cluck():
      print("-- general_trigger: cluck")
      actions.tracking.control_gaze_toggle()
    
    def noise_trigger_tut():
      print("-- general_trigger: tut")
      if (actions.speech.enabled()):
        actions.mouse_click(1)

    
    #def noise_trigger_shush(active: bool):
    #  pass


      #actions.tracking.control_gaze_toggle()
      
        

    
      
      
  