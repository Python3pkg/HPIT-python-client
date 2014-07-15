from client import Plugin

from pymongo import MongoClient

class SkillManagementPlugin(Plugin):
    def __init__(self, entity_id, api_key, logger, args = None):
        super().__init__(entity_id, api_key)
        self.logger = logger
        self.mongo = MongoClient('mongodb://localhost:27017/')
        self.db = self.mongo.hpit_skills


    def post_connect(self):
        super().post_connect()
        
        self.subscribe(
            add_skill=self.add_skill_callback,
            remove_skill=self.remove_skill_callback,
            get_skill=self.get_skill_callback)

    #Skill Management Plugin
    def add_skill_callback(self, message):
        self.logger.debug("ADD_SKILL")
        self.logger.debug(message)

    def remove_skill_callback(self, message):
        self.logger.debug("REMOVE_SKILL")
        self.logger.debug(message)

    def get_skill_callback(self, message):
        self.logger.debug("GET_SKILL")
        self.logger.debug(message)
