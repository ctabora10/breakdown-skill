from mycroft import MycroftSkill, intent_file_handler


class Breakdown(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('breakdown.intent')
    def handle_breakdown(self, message):
        self.speak_dialog('breakdown')


def create_skill():
    return Breakdown()

