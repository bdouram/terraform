import globals
from threading import Thread


class Planet(Thread):
    def __init__(self, distance, terraform, size, name):
        Thread.__init__(self)
        self.distance = distance
        self.terraform = terraform
        self.size = size
        self.name = name

    def print_planet_info(self):
        print(f"🪐 - [{self.name}] → {self.terraform}% HABITABLE")

    def run(self):
        globals.acquire_print()
        self.print_planet_info()
        globals.release_print()

        while(globals.get_release_system() == False):
            pass

        while(True):
            pass
