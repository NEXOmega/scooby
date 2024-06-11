from lcd_print import Display, add_to_print_queue
from utils import module

def on_load():
    add_to_print_queue(DisplayTask("Task Display"))

class DisplayTask(module.Module):
    tasks = ["Aller chercher le paddle", "Faire une etagere pour evoli"]
    def setup_display(self):
        tasks_count = Display(
            "Il reste : {} taches a faire".format(len(self.tasks))
        )
        self.displays_queue.append(tasks_count)

        for task in self.tasks:
            self.displays_queue.append(Display(
                task
            ))