from models.greetings import GreetingsModel
from views.greetings_view import GreetingsView


class GreetingsController:
    def __init__(self, name):
        self.model = GreetingsModel(name)
        self.view = GreetingsView()

    def run(self):
        message = self.model.get_message()
        self.view.return_message(message)
