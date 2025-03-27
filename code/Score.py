from importlib.util import source_hash

import pygame
import os
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, COLOR_PINK, COLOR_WHITE, WIN_HEIGHT, MENU_OPTION
from code.DBProxy import DBProxy

from datetime import datetime

class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/menuCE.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.db_proxy = DBProxy('DBScore')  # Criar a conexão com o banco de dados

        # Definir cores de verde em gradiente
        self.score_colors = [
            (100, 255, 100),  # Verde escuro para o 1º lugar
            (0, 200, 0),      # Verde médio para o 2º lugar
            (0, 160, 0)       # Verde claro para o 3º lugar
        ]

    def save(self, score: int):
        """Salva a pontuação no banco de dados com data formatada"""
        data = {
            'score': score,
            'date': datetime.now().strftime('%d/%m %H:%M')  # Formato: Dia/Mês Hora:Minuto
        }
        self.db_proxy.save(data)

    def read_scores(self):
        """Lê as 3 melhores pontuações do banco de dados"""
        return self.db_proxy.retrieve_top10()

    def show(self):
        pygame.mixer_music.load(f'./asset/score.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            # Instruções para voltar no topo
            self.score_text(20, "Press ESC to return", COLOR_WHITE, (WIN_WIDTH / 2, 30))

            # Título da tela de scores
            self.score_text(50, "High Scores", COLOR_PINK, (WIN_WIDTH / 2, 100))

            # Ler e mostrar pontuações do banco de dados
            scores = self.read_scores()

            for i, score_data in enumerate(scores, 1):
                score = score_data[1]  # O score está na segunda posição (índice 1)
                date = score_data[2]   # A data está na terceira posição (índice 2)
                score_text = f"{i}. {score} ({date})"
                color = self.score_colors[i - 1] if i <= 3 else COLOR_WHITE
                self.score_text(35, score_text, color, (WIN_WIDTH / 2, 200 + 40 * (i - 1)))

            pygame.display.flip()

            # Processar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            clock.tick(30)

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='palatinolinotype', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)