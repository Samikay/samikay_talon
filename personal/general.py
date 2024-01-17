import os
import time

from talon import Context, Module, actions, app, clip, cron, ctrl, imgui, ui
from talon_plugins import eye_zoom_mouse

self = actions.self

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
  def toggle_speech():
    """enables discord (via api) and disables talon and vice versa - hook up to a foot switch press for maximum ease of use"""
    if actions.speech.enabled():
      actions.user.discord_set_mute_status(False)
      actions.speech.disable()
    else:
      actions.user.discord_set_mute_status(True)
      actions.speech.enable()
    

  

@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Click"""
        if (actions.tracking.control_zoom_enabled()):
          actions.skip()
        else:
          actions.mouse_click(0)
  