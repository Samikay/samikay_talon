app: intothebreach
-

tag(): user.game_window

# Set game to windowed mode and say 'game window resize' to have mouse positions sync ud p here.
settings():
    user.game_window_size_x = 1282
    user.game_window_size_y = 752
    user.mouse_move_amount = 20

# --- Actions
<user.arrow_key> [<user.n9>]: user.game_itb_mouse_dir(arrow_key, n9 or 1)


# air -> acid rebind as 'air' isn't picked up as often.
# letters: (a)cid, (d)rum, (s)un, (f)ine
acid: key(a)
save acid: user.game_itb_move_and_save("a")
save <user.letter>: user.game_itb_move_and_save(letter)
go acid: user.game_itb_goto_char("a")
go <user.letter>: user.game_itb_goto_char(letter)


move undo: key(shift)
turn reset: key(backspace)
turn end: key(space)

center: 
    user.mouse_move_center_active_window()
    sleep(50ms)
    user.mouse_move_relative(0, -15)
    
mouse info: user.mouse_move_relative_window(79,671)
mouse status: user.mouse_move_relative_window(98,565)

deploy: user.game_itb_confirm_deployment()
continue: 
    user.mouse_move_relative_window(1001,657)

whoops: user.mouse_move_relative_window(707,414)
confirm: user.mouse_move_relative_window(566,414)

understood: user.mouse_move_relative_window(682,523)

pod open: user.mouse_move_relative_window(960,488)
pod one: user.mouse_move_relative_window(725,428)
pod two: user.mouse_move_relative_window(735,548)

mech install: user.mouse_move_relative_window(467,491)
mech undo: user.mouse_move_relative_window(467,550)
mech health: user.mouse_move_relative_window(609,279)
mech move: user.mouse_move_relative_window(762,279)
mech storage: user.mouse_move_relative_window(951,302)
mech weapon one: user.mouse_move_relative_window(609,495)
mech weapon two: user.mouse_move_relative_window(609,546)

rep spend: user.mouse_move_relative_window(638,652)
rep weapon: user.mouse_move_relative_window(377,227)
rep supply: user.mouse_move_relative_window(816,227)
rep donate: user.mouse_move_relative_window(401,438)
rep right: user.mouse_move_relative(95,0)
rep left: user.mouse_move_relative(-95,0)

mouse weapon: user.mouse_move_relative_window(278,664)

#mishearing
ten: mimic("down")