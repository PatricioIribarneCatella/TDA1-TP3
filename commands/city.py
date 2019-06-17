class City():

    def __init__(self, name):
        self._name = name
        self._player = None
        self._production = 0
        self._armies = 0

    def get_name(self):
        return self._name

    def get_production(self):
        return self._production

    def get_armies(self):
        return self._armies

    def get_player(self):
        return self._player

    def set_player(self, player):
        self._player = player

    def set_armies(self, armies):
        self._armies = armies

    def set_production(self, production):
        self._production = production

    def is_metropolis(self):
        return False
