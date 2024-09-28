from hangman_logic import hangman_logic, console_GUI

class hangman_game():
    def __init__(self) -> None:
        self.logic = hangman_logic()
        self.GUI = console_GUI(gallow_list=self.logic.gallow_list, word = self.logic.word)

    def start_game(self):
        self.GUI.print_rules()
        self.GUI.print_gallow()
        self.GUI.print_hidden_word()
        self.game_loop()

    def game_loop(self):
        while True:
            output = self.GUI.print_input_letter().lower()
            if output == 'exit':
                break
            if  len(output) == 1 and type(output) is str:
                output = self.logic.compare_letter_with_word(output)
                if output[0]:
                    self.GUI.correct_answer()
                    self.GUI.change_hidden_word(index=output[1], letter=output[2])
                    self.GUI.print_gallow()
                    self.GUI.print_hidden_word()
                    if self.logic.is_word_complited(self.GUI.hidden_word):
                        self.GUI.congratz()
                        break
                else:
                    self.GUI.incorrect_answer()
                    if self.GUI.build_gallow(self.logic.word):
                        break
                    self.GUI.print_gallow()
                    self.GUI.print_hidden_word()




