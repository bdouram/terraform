from threading import Thread
import globals

class Planet(Thread):
    def __init__(self, distance, terraform, size, name):
        Thread.__init__(self)
        self.distance = distance
        self.terraform = terraform
        self.size = size
        self.name = name

    def nuke_detected(self):
        while(self.terraform > 0):
            before_percentage = self.terraform
            while(before_percentage == self.terraform):
                pass
            print(f"[NUKE DETECTION] - The planet {self.name} was bombed. {self.terraform}% UNHABITABLE")

    def print_planet_info(self):
        print(f"🪐 - [{self.name}] → {self.terraform}% UNINHABITABLE")

    def run(self):
        globals.acquire_print()
        self.print_planet_info()
        globals.release_print()

        while(globals.get_release_system() == False):
            pass

        while(True):
            self.nuke_detected()