class Racedata:
    def __init__(self, yr, tm, lps, dst):
        self.year = yr
        self.team = tm
        self.laps = lps
        self.distance = dst

    def __str__(self):
        return '** Le Mans ' + str(self.year) + ' **\n' + str(self.team) + '\n' + str(self.laps) + \
               ' laps, total distance was ' + str(self.distance) + 'km'