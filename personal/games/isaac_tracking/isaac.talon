#mode: user.game
app: boi
-

tag(): user.game_window

settings():
    key_hold = 30
    speech.timeout = 0.085
    user.game_window_size_x = 1600
    user.game_window_size_y = 1024

stop: 
    user.game_keys_down_and_up("", "wasd")
    user.game_arrow_key_exclusive("")

up: user.game_arrow_key_exclusive("up")
left: user.game_arrow_key_exclusive("left")
right: user.game_arrow_key_exclusive("right")
down: user.game_arrow_key_exclusive("down")

move: user.game_isaac_toggle_move()

parrot(tut): user.game_isaac_toggle_move()

track gaze:                 tracking.control_gaze_toggle(true)
track head:                 tracking.control_gaze_toggle(false)

regions: 
    user.game_isaac_setup_regions()
    mimic("grid five")
    mimic("tracking") 

center: user.mouse_move_center_active_window()


##  Copied directly from personal/plugin/mouse.talon
mouse <user.arrow_key> [<user.n9>]: 
    modifier = n9 or 1
    user.mouse_move_dir(arrow_key, 1 * modifier)