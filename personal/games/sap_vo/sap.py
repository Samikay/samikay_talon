import time

from talon import Module, Context, actions

mod = Module()

mod.apps.sap = """
os: windows
and app.exe: Super Auto Pets.exe
"""

mod.apps.sap = """
os: windows
and title: /Super Auto Pets/i
"""


ctx = Context()
ctx.matches = """
app: sap
"""
