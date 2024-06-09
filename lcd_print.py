import time
import threading
from rpi_lcd import LCD

lcd = LCD() 

HOST = "192.168.1.13"
PORT = "6601"

queue = []
queue_index = 0
is_paused = False

class Display:
	def __init__(self, first_line, second_line: str = "", print_time: float = 2, clear_after: bool = False) -> None:
		self.first_line = first_line
		self.second_line = second_line
		self.print_time = print_time
		self.clear_after = clear_after
	

def print_next():
	global queue_index
	next_display = queue[queue_index % len(queue)]
	print_to_lcd(next_display)
	
	time.sleep(next_display.print_time)
	if(next_display.clear_after):
		lcd.clear()

	queue_index = queue_index + 1
	while(is_paused):
		time.sleep(1)
	print_next()

	if queue_index +1 == len(queue):
		queue_index = 0


def print_to_lcd(display: Display):
	if type(display.first_line) == str:
		lcd.text(display.first_line, 1)
	else:
		lcd.text(display.first_line(), 1)

	if type(display.second_line) == str:
		lcd.text(display.second_line, 1)
	else:
		lcd.text(display.second_line(), 2)
		

def add_to_print_queue(display: Display):
	queue.append(display)

def start():
	thread = threading.Thread(target=print_next)
	thread.start()