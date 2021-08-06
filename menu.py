from console_colors import CColors as color


class MenuOption:
    A = 'a.	Read Magic 8 Ball responses from a file'
    B = 'b.	Play Magic Eight Ball'
    C = 'c.	Print out responses and categories alphabetically'
    D = 'd.	Write responses to a file'
    E = 'e. Add magic8 response and category'
    F = 'f. Exit'


class Menu:

    def __init__(self):
        self._menu = f""" 
        ___________________ Magic8 __________________________

        {MenuOption.A}
        {MenuOption.B}
        {MenuOption.C}
        {MenuOption.D}
        {MenuOption.E}
        {MenuOption.F}
        _____________________________________________________
        """

        self._menu_map = {
            'a': MenuOption.A, 
            'b': MenuOption.B,
            'c': MenuOption.C, 
            'd': MenuOption.D,
            'e': MenuOption.E,
            'f': MenuOption.F
        }

        self._selected_menu = None

    def _display(self):
        print(color.MENU, color.BOLD, self._menu)
    
    @property
    def selection(self):
        return self._selected_menu

    def select(self, user=''):
        # Display the menu and capture a menu selection from the user.
        # Implement input validation 
        # Map the selected menu to MenuOption then set the private variable instance
        # _selected_menu 

        self._selected_menu = None
        self._display()
        while not self._selected_menu:
            selection = input('Select a menu option: ').lower()
            if selection not in self._menu_map:
                print(color.FAIL, 'Error: Selected menu option does not exist.'
                                  ' Please try again.', color.ENDC)
                self._display()
                continue
            self._selected_menu = self._menu_map[selection]
