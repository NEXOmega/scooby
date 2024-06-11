from lcd_print import Display, add_to_print_queue
import datetime
import python_weather
import asyncio

from utils import module

def on_load():
    add_to_print_queue(DisplayTime("Time Display"))

async def getweather():
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
    weather = await client.get('Marseille')
    return weather
    
class DisplayTime(module.Module):
    def setup_display(self):
        weather = asyncio.run(getweather())
        time_display = Display(
           lambda : "{} {}deg {}".format(datetime.datetime.now().strftime("%m/%d/%Y"), weather.temperature, datetime.datetime.now().strftime("%H:%M:%S"))
        )
        self.displays_queue.append(time_display)
        