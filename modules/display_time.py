import lcd_print
import datetime
import subprocess

song = subprocess.run(['mpc', '-h','192.168.1.13','-p', '6601', 'current'], stdout=subprocess.PIPE)

#lcd_print.print("Playing", song.stdout.decode('utf-8'))

time = datetime.datetime.now()

test_display = lcd_print.Display(lambda : datetime.datetime.now().strftime("%m/%d/%Y"), lambda : datetime.datetime.now().strftime("%H:%M:%S"), clear_after=False)
def on_load():
    global index
    lcd_print.add_to_print_queue(test_display)