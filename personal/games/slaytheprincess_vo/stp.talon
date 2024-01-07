app: slaytheprincess
-

tag(): user.game_window

settings():
    #speech.timeout = 0.125
    user.mouse_move_amount = 50

# common mis-hearings
ten: mimic("down")
end: mimic("enter")

<user.arrow_key> [<user.n9>]: user.game_stp_option_dir(arrow_key, n9 or 1)

pick: user.mouse_move_relative_window(1875,98)

history: user.game_move_click(708,1098)
save: user.game_move_click(1043,1093)
load: user.mouse_move_relative_window(1141,1092)
return: user.game_move_click(142,1035)

bottom: 
    user.game_stp_option_dir("down", 20)
    mimic("wheel down")


# Skip cutscenes
skip:
    mouse_click(0)
    sleep(1s)
    mouse_click(0)
    sleep(50ms)
