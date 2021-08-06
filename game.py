from responses import Responses 
from magic8 import Magic8
from menu import Menu, MenuOption
from console_colors import CColors as c
import time


class GameLoop:
    def __init__(self):
        self._done = False
        self._responses_object = None # Responses instance 
        self._magic8 = None # Magic8 instance 
        self._menu = Menu()
        self._keep_asking = True

    def start(self, user=None):
        # This function implements the entire game loop 
        # Displays the menu 
        # captures input 
        # Invokes the appropriate function for each menu option.
        self._menu.select()

        while not self._done:
            selection = self._menu.selection

            if selection == MenuOption.A:
                print(c.BLUE, 'Executing Menu Option A')
                self._responses_object = Responses('input.txt')
                self._responses_object.read()

            elif selection == MenuOption.B:
                if not self._responses_object:
                    print(c.FAIL, 'You have not loaded in any responses yet,'
                          ' make sure to read responses from a file first')
                else:
                    self._keep_asking = True
                    self._magic8 = Magic8(self._responses_object)
                    print(c.BLUE, 'Executing Menu Option B', c.MENU)
                    initial_question = input('Ask the Magic 8 Ball'
                                             ' a question: ')
                    self._magic8.shake()
                    while self._keep_asking:
                        question = input('Ask the Magic 8 Ball a question, '
                                         'enter a blank line to exit: ')
                        if question == "":
                            self._keep_asking = False
                        else:
                            self._magic8.shake()

            elif selection == MenuOption.C:
                print(c.BLUE, 'Executing Menu Option C', c.CYAN)
                self._responses_object.display()

            elif selection == MenuOption.D:
                print(c.BLUE, 'Executing Menu Option D')
                self._responses_object.write()

            elif selection == MenuOption.E:
                print(c.BLUE, 'Executing Menu Option E')
                self._responses_object.add()

            elif selection == MenuOption.F:
                print(c.BLUE, 'Thank you for playing!')
                self._end()
                continue

            self._menu.select()

    def _end(self):
        self._done = True
