import time
import textwrap
import threading
from rpi_lcd import LCD

lcd = LCD() 

HOST = "192.168.1.13"
PORT = "6601"

queue = []
queue_index = 0
is_paused = False

class Display:
	def __init__(self, text: str, print_time: float = 5, clear_after: bool = True) -> None:
		self.text = text
		self.print_time = print_time
		self.clear_after = clear_after
	
	def print(self):
		text = self.text
		if type(self.text) != str:
			text = self.text()
		lines = textwrap.wrap(text, 16, break_long_words=False)
		
		for i in range(0, len(lines)-1):
			lcd.text(lines[i], 1)
			lcd.text(lines[i+1], 2)
			time.sleep(self.print_time / (len(lines)-1))
	
	def clear(self):
		lcd.clear()
	

def print_next():
	global queue_index
	next_display = queue[queue_index % len(queue)]
	next_display.print_displays()

	queue_index = queue_index + 1
	while(is_paused):
		time.sleep(1)
	print_next()

	if queue_index +1 == len(queue):
		queue_index = 0
		

def add_to_print_queue(display: Display):
	queue.append(display)

def start():
	thread = threading.Thread(target=print_next)
	thread.start()