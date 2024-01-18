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
  
  def util_dir_to_wasd(dir: str, qe: bool = False):
    """Takes an arrow key, returns wasd. If qe = true, left/right -> q/e"""
    if (qe == False):
      if (dir == "up"): return "w"
      if (dir == "left"): return "a"
      if (dir == "down"): return "s"
      if (dir == "right"): return "d"
    
    if (qe):
      if (dir == "left"): return "q"
      if (dir == "right"): return "e"

    return "w"



  def util_print_active_window(): 
    "Prints window title"
    #If you're interested in other attributes (e.g. whether it's fullscreen) open REPL and print(dir(ui.active_window())
    window = ui.active_window()
    print(f"Title: {window.title}, rect: {window.rect}, size: {window.rect.size}, id: {window.id}")





