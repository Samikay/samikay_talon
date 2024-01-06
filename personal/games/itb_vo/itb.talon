app: intothebreach
-



settings():
    user.mouse_move_amount = 20

# --- Actions
# Override these command to null it out. 
snap full: user.copy_mouse_position_relative_window()
ignore close: user.copy_mouse_position_relative_window()

acid: key(a)
ten: mimic("down")

move undo: key(shift)
turn reset: key(backspace)
turn end: key(space)

save acid: user.game_itb_move_and_save("a")
save <user.letter>: user.game_itb_move_and_save(letter)
go acid: user.game_itb_goto_char("a")
go <user.letter>: user.game_itb_goto_char(letter)

center: 
    user.mouse_move_center_active_window()
    sleep(50ms)
    user.mouse_move_relative(0, -15)
    
mouse info: user.mouse_move_relative_window(79,671)

deploy confirm: user.game_itb_confirm_deployment()
mission complete: 
    user.mouse_move_relative_window(1001,657)

whoops: user.mouse_move_relative_window(707,414)
confirm: user.mouse_move_relative_window(566,414)


mech install: user.mouse_move_relative_window(467,491)
mech undo: user.mouse_move_relative_window(467,550)
mech health: user.mouse_move_relative_window(609,279)
mech move: user.mouse_move_relative_window(762,279)
mech storage: user.mouse_move_relative_window(951,302)
mech weapon one: user.mouse_move_relative_window(609,495)
mech weapon two: user.mouse_move_relative_window(609,546)

rep weapon: user.mouse_move_relative_window(377,227)
rep supply: user.mouse_move_relative_window(816,227)
rep right: user.mouse_move_relative(95,0)
rep left: user.mouse_move_relative(-95,0)

<user.arrow_key> [<user.n20>]: user.game_itb_mouse_dir(arrow_key, n20 or 1)


# Skip cutscenes
skip:
    mouse_click(0)
    sleep(1s)
    mouse_click(0)
    sleep(50ms)
