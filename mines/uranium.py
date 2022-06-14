import globals
from threading import Thread

class StoreHouse(Thread):

    def __init__(self, unities, location):
        Thread.__init__(self)
        self.unities = unities
        self.location = location


    def print_store_house(self):
        print(f"🔨 - [{self.location}] - {self.unities} uranium unities are produced.")

    def run(self):
        globals.acquire_print()
        self.print_store_house()
        globals.release_print()

        while(globals.get_release_system() == False):
            pass

        while(True):
            i = 0