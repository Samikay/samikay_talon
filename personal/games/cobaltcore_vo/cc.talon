app: cobaltcore
-

tag(): user.game_window

# Don't think you can change the window size, after setting fullscreen off the window was 1584,1054 (check by saying 'print title' and check the Scripting -> View Log)
#   these were the values I had if you need to reverse engineer some positions?
settings():
    speech.timeout = 0.125
    user.mouse_move_amount = 50
    user.game_window_size_x = 1584
    user.game_window_size_y = 1054

    

# --- Actions
<user.arrow_key> [<user.n9>]: user.game_cc_mouse_dir(arrow_key, n9 or 1)

acid: user.game_hold_key("a")
drum: user.game_hold_key("d")
space: 
    user.game_hold_key("space")
    mimic("cards")

ten: mimic("down")

righty: user.game_hold_mouse(1)

center: 
    user.mouse_move_center_active_window()
    sleep(10ms)
    user.mouse_move_relative(0, -20)

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

mid row: user.mouse_move_relative_window(932,415)
mid right: mimic("mouse right")
mid left: mimic("mouse left")



