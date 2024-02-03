tag: user.game_window
-

# Change grid commands to stay within our window
grid: mimic("grid win")

grid <user.number_key>+: 
    mimic("grid win")
    user.grid_narrow_list(number_key_list)


# Utility
copy mouse: user.copy_mouse_position_relative_window() 

game window resize: user.game_resize_window()

# These are commands we null out to not mess with our window.
snap full: skip()
ignore close: skip()
snap right: skip()
snap left: skip()