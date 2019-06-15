class Metropolis(City):

    def __init__(self, name, production, player):
        City.__init__(self, name, production)
        self._player = player

    def is_metropolis():
        return True
