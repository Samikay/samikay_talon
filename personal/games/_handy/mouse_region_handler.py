from talon import ui, actions

class MouseRegionHandler:
    def __init__(self):
        self.rect = None
        self.regions = []

    def setup(self, width: int, height: int):
        windowRect = ui.active_window().rect
        print(f"windowRect: {windowRect}")
        center_x, center_y = windowRect.left + (windowRect.width / 2), windowRect.top + (windowRect.height / 2)
        self.rect = ui.Rect((center_x - width / 2) - windowRect.left, (center_y - height / 2) - windowRect.top, width, height)

        # center: 883, 497
        # 0: 664,622
        self.regions = []

        #bottom left, follow mouse grid
        startingRegion = ui.Rect(self.rect.left - width, self.rect.top + height, width, height)

        print(f"center: ({center_x},{center_y}) self.rect: {self.rect}, starting: {startingRegion}")
        
        for row in range(0, 3):
            for col in range(0, 3):
                regionRect = ui.Rect(startingRegion.left + col * width, startingRegion.top - row * height, width, height)
                self.regions.append(regionRect)


    def which(self, closest:bool, evensOnly: bool) -> int:
        x,y = actions.user.mouse_position_relative_window()
        for idx, r in enumerate(self.regions):
            #print(f"is {x},{y} ---> {r} [{r.contains(x,y)}]")
            if (r.contains(x, y)):
                return (idx+1)

        if (closest):
            point = ui.Point2d(x, y)
            ret = -1  
            smallest_d = 10000
            for idx, r in enumerate(self.regions):
                if (evensOnly and (idx+1) % 2 != 0): continue
                distance = r.distance(point)
                if (distance < smallest_d):
                    ret = idx
                    smallest_d = distance
            
            return (ret+1)

        return -1


    def which_inclusive(self, left: str = "a", up: str = "w", right: str = "d", down: str = "s") -> str:
        leftRegions = [1,4,7]
        rightRegions = [3,6,9]
        downRegions = [1,2,3]
        upRegions = [7,8,9]

        region = self.which(True, False)

        keys = ""
        if (region in leftRegions): keys += left
        if (region in upRegions): keys += up
        if (region in rightRegions): keys += right
        if (region in downRegions): keys += down

        return keys

    def which_dir_exclusive(self, left: str = "left", up: str = "up", right: str = "right", down: str = "down") -> str:
        region = self.which(True, True)
        if (region == 2): return down
        if (region == 4): return left
        if (region == 6): return right
        if (region == 8): return down