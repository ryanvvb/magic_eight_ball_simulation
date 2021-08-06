from game import GameLoop
import os 

# os.chdir('PA')

if __name__ == '__main__':
    print("\n")
    print('This is a simulation of a Magic 8 Ball toy.  After entering your'
          ' name, a menu will appear that you can interact with.  The program'
          ' can read responses for the magic 8 ball from a file, you can '
          'sort and print the responses to the console, add your own responses,'
          ' print the responses to file, and play the Magic 8 Ball game.  '
          'In the game, you can ask provide an input question and the 8 ball '
          'will read your future and provide a response.  Of course the 8 ball'
          ' can not actually see into the future, instead the program will '
          'generate a pseudo-random number and return the matching response.'
          '  Have fun playing!')
    gamer = None
    while not gamer or len(gamer) == 0:
        gamer = str(input("Enter your name: "))
    print(f"Hi {gamer}")
    game = GameLoop()
    game.start(gamer)
