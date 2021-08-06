from responses import Responses
import random
from console_colors import CColors as c

class Magic8:

    def __init__(self, responses: Responses):
        self._responses = responses

    def shake(self): 
        # This function returns a random response from a list of magic8 responses
        # Use random module to generate a random index between 0 and length or responses
        random_number = random.randint(0, len(self._responses.responses) - 1)

        game_list = [(k, v) for k, v in self._responses.responses.items()]
        fortune = game_list[random_number]
        return print(fortune)
