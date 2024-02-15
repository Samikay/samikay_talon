
# See wow for an example. Game mode has none of the normal commands so you must define everything you want.
#   Why would you want to do this? To provide less commands for Talon to try and match against, a slimmer command
#   list is less chance for errors :) Useful for real-time games!
^game mode$:                user.game_mode_enable()



