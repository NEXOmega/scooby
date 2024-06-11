from time import sleep
import lcd_print

class Module:
    displays_queue = []
    def __init__(self, name: str):
        self.name = name

        self.setup_display()
    
    def setup_display(self):
        pass
    
    def print_displays(self):
        for display in self.displays_queue:
            display.print()

            if(display.clear_after):
                display.clear()
