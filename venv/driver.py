
class Driver:
    def __init__(self, name, nat):
        self.last = name[1]
        self.first = name[0]
        self.nationality = nat

    def __str__(self):
        return '' + self.last + ', ' + self.first + ' (' + self.nationality + ')'