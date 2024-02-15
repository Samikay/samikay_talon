from talon import ui, actions, ctrl

class InputHolder:
    def __init__(self):
        self.last_held_key = ""
        self.holding_key = False
        self.holding_click = False

    def reset(self, heldKey = True, heldClick = True):
        if (heldKey): self.holding_key = False
        if (heldClick): self.holding_click = False
        
    def hold_key(self, key: str) -> bool:
        self.holding_key = not self.holding_key
        if (key != self.last_held_key): 
            actions.user.game_key_hold_down("", self.last_held_key)
            self.last_held_key = key

        if (self.holding_key):
            actions.user.game_key_hold_down(key, "")
        else:
            actions.user.game_key_hold_down("", key)
        print(f"{self.holding_key} -> {key}")
        return self.holding_key
    
    def hold_click(self, button: int):
        self.holding_click = not self.holding_click
        if (self.holding_click):
            ctrl.mouse_click(button, down=True)
        else:
            ctrl.mouse_click(button, up=True)
  

  

