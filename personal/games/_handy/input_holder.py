from talon import ui, actions, ctrl, cron

class InputHolder:
    def __init__(self, debug=False):
        self.last_held_key = ""
        self.holding_key = False
        self.holding_click = False
        
        self.interval_click = 1
        self.interval_click_cron = None

        self.debug = debug

    def resetKey(self): 
        self.holding_key = False
        self.interval_click_cancel()

    def resetClick(self):
        self.holding_click = False

    def release_key(self):
        if (self.holding_key):
            actions.user.game_key_hold_down("", self.last_held_key)
            self.last_held_key = ""
            self.resetKey()
            if (self.debug): print(f"Release Key: {self.last_held_key}")

    def get_last_held(self) -> str:
        return self.last_held_key
    
    def hold_key(self, key: str) -> bool:
        if (len(key) <= 0): return self.holding_key
        self.holding_key = not self.holding_key
        if (key != self.last_held_key):
            if (len(self.last_held_key) > 0):
                actions.user.game_key_hold_down("", self.last_held_key)
                if (self.debug): print(f"Key Hold - Releasing last held: {self.last_held_key}")
            self.last_held_key = key

        if (self.holding_key):
            actions.user.game_key_hold_down(key, "")
        else:
            self.resetKey()
            actions.user.game_key_hold_down("", key)
        if (self.debug): print(f"Key Hold: {self.holding_key} -> {key}")
        return self.holding_key

    def is_holding_click(self) -> bool:
        return self.holding_click
    
    def hold_click(self, button: int):
        self.holding_click = not self.holding_click
        if (self.holding_click):
            ctrl.mouse_click(button, down=True)
        else:
            ctrl.mouse_click(button, up=True)
        if (self.debug): print(f"Mouse Hold: {self.holding_click} -> {button}")



    # ARPG functionality, hold one key while trying the other (discovery: can't be a key, has to be a click)
    def interval_click_while_holding(self, button: int): 
        self.interval_click = key
        if (self.interval_click_cron is None):
            self.interval_click_cron = cron.interval("200ms", lambda: self.cron_try_click())

    def interval_click_cancel(self):
        cron.cancel(self.interval_click_cron)
        self.interval_click_cron = None


    def cron_try_key(self):
        if (self.holding_key):
            ctrl.mouse_click(self.interval_click)

            # Can't use another key, unfortunately, otherwise the key() recognition for pedals goes crazy?
            # Luckily we can still use mouse clicks.
            #actions.key(f"{self.interval_click}:down")
            #actions.key(f"{self.interval_click}:up")
        else:
            self.interval_click_cancel()



  

  

