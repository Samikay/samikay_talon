#mode: user.game
app: bokura
-

# Must be in game mode, say 'game mode' to run. 'command mode' to return back to normal Talon.
settings():
    key_hold = 30
    speech.timeout = 0.085

stop: 
    user.game_keys_down_and_up("", "wasd")
    user.game_arrow_key_exclusive("")

up: user.game_arrow_key_exclusive("up")
left: user.game_arrow_key_exclusive("left")
right: user.game_arrow_key_exclusive("right")
down: user.game_arrow_key_exclusive("down")

grab: user.game_key_hold_down("enter", "")
release: user.game_key_hold_down("", "enter")

#parrot(tut): user.game_bokura_toggle_enter()
#parrot(whistle): print("whistle")


jump: mimic('space')

#parrot(tut): user.game_key_hold_down("enter", "")

^setup regions$: mimic('regions')

regions: 
    user.game_bokura_setup_regions()
    mimic("grid win")
    mimic("grid five")
    mimic("tracking") 

center: user.mouse_move_center_active_window()

##  Copied directly from personal/plugin/mouse.talon
mouse <user.arrow_key> [<user.n9>]: 
    modifier = n9 or 1
    user.mouse_move_dir(arrow_key, 1 * modifier)