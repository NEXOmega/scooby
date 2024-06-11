from lcd_print import Display, add_to_print_queue
import subprocess
from utils import module



def get_song() -> str:
    song = subprocess.run(['mpc', '-h','192.168.1.13','-p', '6601', 'current'], stdout=subprocess.PIPE)
    return song.stdout.decode()


def on_load():
    add_to_print_queue(DisplayQuote("Quote Display"))

class DisplayQuote(module.Module):
    def setup_display(self):
        quote_display = Display(
            "Playing : {}".format(get_song())
        )
        self.displays_queue.append(quote_display)