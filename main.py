from controllers.greetings_controller import GreetingsController
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = None

    controller = GreetingsController(name)
    controller.run()
