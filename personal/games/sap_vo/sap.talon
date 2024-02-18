app: sap
-

# Set game to windowed mode and say 'game window resize' to have mouse positions sync up here.
settings():
    user.mouse_move_amount = 115
    user.game_window_size_x = 1468
    user.game_window_size_y = 904

tag(): user.game_window

# --- Actions

# Common mishearing....
grave three: mimic("grab three")

# Shop spaces
(grab one):   user.game_move_click(275, 600)
(grab two):   user.game_move_click(385, 600)
(grab three): user.game_move_click(495, 600)
(grab four):  user.game_move_click(605, 600)
(grab five):  user.game_move_click(715, 600)

food [one]: user.game_move_click(1175, 600)
food two: user.game_move_click(1065, 600)

# Team spaces, preface "slot" to guarantee no mishearing (mostly unneeded).
[slot] one:   user.game_move_click(275, 350)
[slot] two:   user.game_move_click(385, 350)
[slot] three: user.game_move_click(495, 350)
[slot] four:  user.game_move_click(605, 350)
[slot] five:   user.game_move_click(715, 350)

# 'Roll' was not picked up as often, so 'next' works great.
(next|refresh): user.game_move_click(150, 800)

battle: user.game_move_click(1400, 800)

(freeze|sell): user.game_move_click(800, 800)

confirm: user.game_move_click(947,513)
cancel: user.game_move_click(530,504)

click: mouse_click(0)

unlock open: user.game_move_click(1359, 69)
unlock close: user.game_move_click(1237, 75)

# Open menu
menu: user.game_move_click(1415, 69)
# Click menu items
go exit: user.game_move_click(1254, 442)
go next: user.game_move_click(1254, 347)
go again: user.game_move_click(699, 382)
