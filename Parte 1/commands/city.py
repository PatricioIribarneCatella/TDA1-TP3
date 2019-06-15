class City():

    def __init__(self, name):
        self._name = name
        self._player = None
        self._production = 0
        self._armies = 0

    @property
    def name(self):
        return self._name

    @property
    def production(self):
        return self._production

    @property
    def armies(self):
        return self._armies

    @property
    def player(self):
        return self._player

    def set_player(player):
        self._player = player

    def set_armies(armies):
        self._armies = armies

    def set_production(production):
        self._production = production

    def is_metropolis():
        return False
