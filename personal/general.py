import os
import time

from talon import Context, Module, actions, app, clip, cron, ctrl, imgui, ui
from talon_plugins import eye_zoom_mouse

self = actions.self

mod = Module()
ctx = Context()

pop_click = True

@mod.action_class
class Actions:
  def toggle_speech():
    """enables discord (via api) and disables talon and vice versa - hook up to a foot switch press for maximum ease of use"""
    # Follow the steps in apps/discord/discord_api , you can use localhost (https://127.0.0.1) as the redirect URI.
    if actions.speech.enabled():
      actions.speech.disable()
      #actions.user.microphone_select(1) # Optional, selects 'none' microphone (so you can't make noises/'talon wake' commands)
      actions.user.discord_set_mute_status(False)
    else:
      actions.speech.enable()
      #actions.user.microphone_select(2) # Reselects system default microphone
      actions.user.discord_set_mute_status(True)

  def toggle_pop_click():
    "Toggles pop_click"
    global pop_click
    pop_click = not pop_click


    

  

@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        """Click"""
        if (pop_click):
          actions.mouse_click(0)
  