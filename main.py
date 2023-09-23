from controllers.credit_controller import CreditController
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     name = sys.argv[1]
    # else:
    #     name = None

    controller = CreditController()
    controller.load_existing_menu()
