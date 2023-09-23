from controllers.credit_controller import CreditController
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     name = sys.argv[1]
    # else:
    #     name = None
    print("Credit Simulator")
    controller = CreditController()
    controller.calculate_new_input()
    print("==========")
    print("Load Existing Calculations from API")
    controller.load_existing_menu()
