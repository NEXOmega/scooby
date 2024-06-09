import lcd_print
import random

quote = ["Mange ta main", "Hypixel > All"]

test_display = lcd_print.Display("Random Quote : ", lambda : random.choice(quote) , clear_after=False)
def on_load():
    global index
    lcd_print.add_to_print_queue(test_display)