from mycroft import MycroftSkill, intent_file_handler


class Whybundy(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('whybundy.intent')
    def handle_whybundy(self, message):
        self.speak_dialog('whybundy')


def create_skill():
    return Whybundy()

