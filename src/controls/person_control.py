from src.controls.control import Control


class PersonControl(Control):

    def process(self):
        self.view_menu()
        option = self.read_input()
        self.serve_section(option)

    def view_menu(self):
        print("1. Register")
        print("2. Update")
        print("3. Delete")
        print("4. Display all")
        print("5. Back to Main menu")
        print("------------------------------------------------")

    def read_input(self):
        print("Select section number: ")
        return input()
