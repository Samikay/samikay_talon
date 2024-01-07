import os
import time

from talon import Context, Module, actions, app, clip, cron, ctrl, imgui, ui
from talon_plugins import eye_zoom_mouse

self = actions.self

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
  def util_dir_to_xy(dir: str, v: int = 1):
    """Takes a dir and returns the x,y"""
    x, y = 0, 0
    if (dir == "up"): y = -1;
    if (dir == "down"): y = 1;
    if (dir == "left"): x = -1;
    if (dir == "right"): x = 1;
    x = x*v
    y = y*v
    return (x, y)

  def util_dir_to_diag_xy(dir: str, v: int = 1):
    """Takes a dir and returns a diagonal x,y"""
    x, y = 0, 0
    if (dir == "up"): x = -1; y = -1;
    if (dir == "down"): x = 1; y = 1;
    if (dir == "left"): x = -1; y = 1;
    if (dir == "right"): x = 1; y = -1;
    x = x*v
    y = y*v
    return (x, y)


