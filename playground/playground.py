"""
Class which represents the virtual environment for virtual bots
"""

#TODO: make scenario object class for static objects
#TODO: make physics class

from basestation.bot.base_station_bot import BaseStationBot

class Playground():
    def __init__(self, playground_id, is_private):
        self.name = ""
        self.playground_id = playground_id
        self.sessions = []
        self.is_active = True
        self.is_private = is_private
        self.scenario = []
        self.bots = {}

    def add_session_to_playground(self, session_id):
        self.sessions.append(session_id)

    def get_session_id(self):
        return self.session_id

    def set_playground_name(self, name):
        self.name = name

    def get_playground_id(self):
        return self.playground_id

    def is_active(self):
        return self.is_active;

    def is_private(self):
        return self.is_private

    def add_scenario(self, scenario_object):
         self.scenario.append(scenario_object)

    def add_bot(self, bot):
        self.bots[bot.get_id] = bot

    #TODO: simbot class - move function!
    def move_simbot(self, direction):
        if self.is_private:
            #apply physics to direction
            #self.bots[0].move(direction)
            pass