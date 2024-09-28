from hangman_words import random_word
import time
class hangman_logic():
    def __init__(self) -> None:
        self.gallow_list : list[str] = ['|\n|\n|', '+---\n|\n|\n|','+------\n|     O\n|\n|','+------\n|    O\n|    ()\n|','+------\n|    O\n|    <()>\n|','+------\n|    O\n|   <()>\n|    〈〉']
        self.word = random_word()

    def compare_letter_with_word(self, letter):
        if letter in self.word:
            return True, [i for i, j in enumerate(self.word) if j == letter], letter
        else:
            return False, 
    
    def is_word_complited(self, hidden_word):
        if self.word == hidden_word:
            return True

class console_GUI():
    def __init__(self, gallow_list, word) -> None:
        # self.logic = hangman_logic()
        # self.gallow_list = self.logic.gallow_list
        self.gallow_list = gallow_list
        self.hidden_word = ['_' for _ in word]

    def change_hidden_word(self, index, letter):
        for idx in index:
            self.hidden_word[idx] = letter

    def build_gallow(self, word):
        self.gallow_list.pop(0)
        if len(self.gallow_list) == 1:
            self.print_gallow()
            print("Gallow is constructed, you loose!")
            self.print_game_over(word)
            return True
    
    def print_game_over(self, word):
        print("GAME OVER!")
        print("Word that was hidden: ", word)

    def incorrect_answer(self):
        print("You are wrong!!!")

    def correct_answer(self):
        print("You are right! Keep up!")

    def print_gallow(self):
        print(self.gallow_list[0])

    def print_rules(self):
        print(f"""You have to discover what word is hidden 
              \n For that u have {len(self.gallow_list)} lives or chances to be wrong
              \n Each mistake will draw one piece of a hangman
              \n When hangman will be drawn full you will lose""")

    def print_lives(self):
        print(f"You have {len(self.gallow_list)} yet")

    def print_hidden_word(self):
        print(f"You have to find out what word is hidden between underscores: ", self.hidden_word)

    def print_input_letter(self):
        return input(f'Write letter you think may be hidden in word\n')
    
    def congratz(self):
        print("U win!!!")