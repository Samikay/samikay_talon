app: sap
-

settings():
    user.mouse_move_amount = 115

tag(): user.game_window

# --- Actions
# Override these command to null it out. 
grave three: mimic("grab three")

(grab one):   user.game_sap_moveto_click(275, 600)
(grab two):   user.game_sap_moveto_click(385, 600)
(grab three): user.game_sap_moveto_click(495, 600)
(grab four):  user.game_sap_moveto_click(605, 600)
(grab five):  user.game_sap_moveto_click(715, 600)

food [one]: user.game_sap_moveto_click(1175, 600)
food two: user.game_sap_moveto_click(1065, 600)

one:   user.game_sap_moveto_click(275, 350)
two:   user.game_sap_moveto_click(385, 350)
three: user.game_sap_moveto_click(495, 350)
[slot] four:  user.game_sap_moveto_click(605, 350)
five:  user.game_sap_moveto_click(715, 350)


(next|refresh): user.game_sap_moveto_click(150, 800)

battle: user.game_sap_moveto_click(1400, 800)

(freeze|sell): user.game_sap_moveto_click(800, 800)

click: mouse_click(0)

unlock open: user.game_sap_moveto_click(1359, 69)
unlock close: user.game_sap_moveto_click(1237, 75)

menu: user.game_sap_moveto_click(1415, 69)

go exit: user.game_sap_moveto_click(1254, 442)
go next: user.game_sap_moveto_click(1254, 347)
go again: user.game_sap_moveto_click(699, 382)

# Skip cutscenes
skip:
    mouse_click(0)
    sleep(1s)
    mouse_click(0)
    sleep(50ms)
