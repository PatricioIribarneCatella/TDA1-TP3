from commands.city import City

class Metropolis(City):

    def __init__(self, name, player):
        City.__init__(self, name)
        self._player = player

    def is_metropolis(self):
        return True
