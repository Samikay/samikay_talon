tag: user.game_window
-

grid: mimic("grid win")

grid <user.number_key>+: 
    mimic("grid win")
    user.grid_narrow_list(number_key_list)

copy mouse: user.copy_mouse_position_relative_window() 

snap full: skip()
ignore close: skip()
snap right: skip()
snap left: skip()