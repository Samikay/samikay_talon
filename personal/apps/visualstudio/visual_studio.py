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

"""
@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        "Null out the pop when working in vs"
   """     