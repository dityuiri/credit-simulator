class GreetingsModel:
    def __init__(self, name=None):
        self.name = name

    def get_message(self):
        if self.name:
            return f"Hello, {self.name}"

        return "Hello, World!"
