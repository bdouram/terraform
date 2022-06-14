import globals
from threading import Thread
from space.rocket import Rocket


class SpaceBase(Thread):
    def __init__(self, name, uranium, fuel, rockets):
        Thread.__init__(self)
        self.name = name
        self.uranium = uranium
        self.fuel = fuel
        self.rockets = rockets
        self.constraints = [uranium, fuel, rockets]

    def print_space_base_info(self):
        print(f"🔭 - [{self.name}] → 🪨  {self.uranium}/{self.constraints[0]} URANIUM  ⛽ {self.fuel}/{self.constraints[1]}  🚀 {self.rockets}/{self.constraints[2]}")

    def run(self):
        globals.acquire_print()
        self.print_space_base_info()
        globals.release_print()

        while(globals.get_release_system() == False):
            pass

        while(True):
            if self.name == 'ALCANTARA':
                ab = Rocket('DRAGON')
                ab.launch(globals.get_bases_ref()['alcantara'], globals.get_planets_ref()['mars'])
            pass
