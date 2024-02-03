from talon import Context, Module, actions

ctx = Context()
ctx.matches = r"""
app: visual_studio
"""

ctx = Context()
ctx.matches = r"""
os: windows
app: visual_studio
"""


# Found alternative to what I was trying here