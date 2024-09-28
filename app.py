from hangman_game import hangman_game
if __name__ == '__main__':
    while True:
        game = hangman_game()
        cmnd = input("What u want to do next: S - start game; E - exit \n")
        if cmnd.lower() == 's':
            game.start_game()
        if cmnd.lower() == 'e':
            print('Leaving from the game')
            break