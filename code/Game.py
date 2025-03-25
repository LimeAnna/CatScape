import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.PlayerNameInput import input_player_name
from code.Score import Score
from code.EntityMediator import EntityMediator  # Reset score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            # Reset score at the start of each game loop
            EntityMediator.score = 0

            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1Bg', menu_return)
                level_return = level.run()

                if level_return:  # Se o jogo terminou
                    # Adicionar input de nome antes de salvar o score
                    from code.Const import WIN_WIDTH, WIN_HEIGHT
                    player_name = input_player_name(self.window, EntityMediator.score)

                    # Salvar score com o nome
                    score.save(f"{player_name}:{EntityMediator.score}")
                    score.show()