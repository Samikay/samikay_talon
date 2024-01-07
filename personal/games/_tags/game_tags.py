from talon import Module

mod = Module()
# this declares a tag in the user namespace (i.e. 'user.tabs')
mod.tag("game_window", desc="Commands for easier navigation of a game window")


# You can alter the set of tags whenever you like within your Python
# code. The tags will only be applied if your Context is currently active
# and they are included in the tags property. Note that you must replace the entire
# set of tags at once, you can't individually add and delete them
#ctx.tags = ["user.tabs"]