import os
import globals
from time import sleep
from random import seed

from stars.planet import Planet
from space.bases import SpaceBase
from space.time import SimulationTime
from mines.oil import Pipeline
from mines.uranium import StoreHouse


def main():

    seed(10)
    
    os.system('cls' if os.name == 'nt' else 'clear')

    sleep(0.5)
    print("Loading planets ...\n")
    mars = Planet(620000, 0, 6779, 'MARS')
    io = Planet(628300, 0, 3643, 'IO')
    ganimedes = Planet(628300, 0, 5268, 'GANIMEDES')
    europa = Planet(628300, 0, 3121, 'EUROPA')

    mars.start()
    io.start()
    ganimedes.start()
    europa.start()


    sleep(0.5)
    print("\nLoading space bases ...\n")
    alcantara = SpaceBase('ALCANTARA', 20000, 100, 1)
    canaveral_cape = SpaceBase('CANAVERAL CAPE', 40000, 500, 5)
    moscow = SpaceBase('MOSCOW', 40000, 500, 5)
    moon = SpaceBase('MOON', 30000, 50, 2)

    alcantara.start()
    canaveral_cape.start()
    moscow.start()
    moon.start()


    sleep(0.5)
    print("\nActivating Mines...\n")
    oil_earth = Pipeline(500, 'EARTH')
    oil_moon = Pipeline(200, 'MOON')

    uranium_earth = StoreHouse(200, 'EARTH')
    uranium_moon = StoreHouse(400, 'MOON')

    uranium_earth.start()
    uranium_moon.start()
    oil_earth.start()
    oil_moon.start()


    
    time_simulation = SimulationTime()
    time_simulation.start()

    bases = {
        'alcantara': alcantara,
        'canaveral_cape': canaveral_cape,
        'moscow': moscow,
        'moon': moon
    }

    planets = {
        'mars': mars,
        'io': io,
        'ganimedes': ganimedes,
        'europa': europa
    }
    
    mines = {
        'oil_earth': oil_earth,
        'oil_moon': oil_moon,
        'uranium_earth': uranium_earth,
        'uranium_moon': uranium_moon,
    }

    globals.set_planets_ref(planets)
    globals.set_bases_ref(bases)
    globals.set_mines_ref(mines)
    globals.set_simulation_time(time_simulation)

    sleep(0.5)
    print("\n\n##################################### SIMULATION STARTED #####################################\n")
    globals.set_release_system()


if __name__ == "__main__":
    main()