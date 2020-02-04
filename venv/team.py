
class Team:
    def __init__(self, drv, cnt, nm, cr, mk):
        self.drivers = drv
        self.country = cnt
        self.name = nm
        self.car_brand = cr
        self.make = mk

    def __str__(self):
        racers = ''
        for driver in self.drivers:
            racers += str(driver) + ', '
        racers = racers[:-2]
        return 'Team name: ' + self.name + ' (' + self.country + ')\n' + 'Drivers: ' + \
               racers + '\nCar: ' + self.car_brand + ' ' + self.make
