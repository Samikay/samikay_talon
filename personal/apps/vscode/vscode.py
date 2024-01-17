from talon import Context, Module, actions, app

ctx = Context()

ctx.matches = r"""
os: windows
app: vscode
"""

"""
@ctx.action_class("user")
class OverrideActions:
    def noise_trigger_pop():
        "Null out the pop when working in vscode"
"""        
  