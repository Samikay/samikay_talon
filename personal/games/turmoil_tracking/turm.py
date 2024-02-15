import time

from talon import Module, Context, actions, ctrl

mod = Module()

mod.apps.turmoil = """
os: windows
and app.exe: Turmoil.exe
"""

ctx = Context()
ctx.matches = """
app: turmoil
"""
