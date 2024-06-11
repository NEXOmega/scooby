from lcd_print import Display, add_to_print_queue
import random

from utils import module

def on_load():
    add_to_print_queue(DisplayQuote("Quote Display"))

class DisplayQuote(module.Module):
    text = "Je suis un ananas tres dissident il me faudrait de l'eau"
    def setup_display(self):
        quote_display = Display(
            self.text
        )
        self.displays_queue.append(quote_display)