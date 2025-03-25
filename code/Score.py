import pygame
import os
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, COLOR_PINK, COLOR_WHITE, WIN_HEIGHT, COLOR_ROSA
from code.EntityMediator import EntityMediator  # Import to access current score


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/menuCE.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.score_file = 'scores.txt'

        # Definir cores de verde em gradiente
        self.score_colors = [
            (100, 255, 100), # Verde escuro para o 1º lugar
            (0, 200, 0),  # Verde médio para o 2º lugar
            (0, 160, 0)  # Verde claro para o 3º lugar
        ]

    def save(self, score_entry: str):
        # Ler pontuações existentes
        scores = self.read_scores()

        # Adicionar nova pontuação
        scores.append(score_entry)

        # Ordenar em ordem decrescente baseado no score numérico e manter os 3 maiores
        def parse_score(entry):
            try:
                # Tenta dividir a entrada em nome e pontuação
                parts = entry.split(':')
                if len(parts) == 2:
                    return int(parts[1])
                # Se não conseguir dividir, tenta converter a entrada inteira para int
                return int(entry)
            except (ValueError, IndexError):
                # Se não conseguir converter, retorna 0
                return 0

        # Ordena os scores e mantém os 3 maiores
        scores.sort(key=parse_score, reverse=True)
        scores = scores[:3]

        # Salvar pontuações
        with open(self.score_file, 'w') as f:
            for s in scores:
                f.write(f"{s}\n")

    def read_scores(self):
        # Se o arquivo não existir, criar com scores zerados
        if not os.path.exists(self.score_file):
            with open(self.score_file, 'w') as f:
                f.write("AAA:0\nBBB:0\nCCC:0\n")

        # Ler pontuações
        with open(self.score_file, 'r') as f:
            # Remove linhas em branco e strip
            scores = [line.strip() for line in f.readlines() if line.strip()]

        # Se o arquivo estiver vazio, usa valores padrão
        if not scores:
            scores = ["AAA:0", "BBB:0", "CCC:0"]

        return scores

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

            # Mostrar score atual na tela
            self.score_text(35, f"Current Score: {EntityMediator.score}", COLOR_ROSA, (WIN_WIDTH / 2, 160))

            # Ler e mostrar pontuações
            scores = self.read_scores()

            for i, score_entry in enumerate(scores, 1):
                # Adiciona tratamento caso a entrada não tenha ':'
                if ':' in score_entry:
                    name, score = score_entry.split(':')
                else:
                    name, score = "AAA", score_entry

                score_text = f"{i}. {name} - {score}"
                color = self.score_colors[i - 1] if i <= 3 else COLOR_WHITE
                self.score_text(35, score_text, color, (WIN_WIDTH / 2, 230 + 40 * (i - 1)))

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