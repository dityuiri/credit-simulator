from controllers.credit_controller import CreditController
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Credit Simulator")
    controller = CreditController()

    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        try:
            controller.calculate_new_input_from_file(input_file)
        except Exception as e:
            print(str(e))

    else:
        controller.calculate_new_input()

    print("==========")
    print("Load Existing Calculations from API")
    controller.load_existing_menu()
