from mycroft import MycroftSkill, intent_file_handler


class OpenVscode(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('vscode.open.intent')
    def handle_vscode_open(self, message):
        self.speak_dialog('vscode.open')


def create_skill():
    return OpenVscode()

