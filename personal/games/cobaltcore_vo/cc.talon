app: cobaltcore
-

settings():
    speech.timeout = 0.125
    user.mouse_move_amount = 50
    

# --- Actions
# Override these command to null it out. 
snap full: user.copy_mouse_position_relative_window()
ignore close: user.copy_mouse_position_relative_window()

grid: mimic("grid win")
grid <user.number_key>+: 
    mimic("grid win")
    user.grid_narrow_list(number_key_list)

acid: user.game_hold_key("a")
drum: user.game_hold_key("d")
space: user.game_hold_key("space")

ten: mimic("down")

center: user.mouse_move_center_active_window()

cards: 
    user.mouse_move_center_active_window()
    sleep(10ms)
    user.mouse_move_relative(0, 300)

cards even: 
    user.mouse_move_center_active_window()
    sleep(10ms)
    user.mouse_move_relative(85, 300)

top: user.mouse_move_relative_window(980,234)

show deck: user.game_move_click(153,77)
show map: user.game_move_click(90,77)
deck close: user.game_move_click(1690,1001)
deck cancel: user.game_move_click(957,997)

<user.arrow_key> [<user.n20>]: user.game_cc_mouse_dir(arrow_key, n20 or 1)


# Skip cutscenes
skip:
    mouse_click(0)
    sleep(1s)
    mouse_click(0)
    sleep(50ms)
