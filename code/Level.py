import random
import sys

import pygame.display
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:

    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))

        self.MAX_ENEMIES = 6  # Limite de inimigos ativos
        pygame.time.set_timer(EVENT_ENEMY, 3000)

    def run(self):
        pygame.mixer_music.load(f'./asset/level1.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    enemy_count = sum(isinstance(ent, Entity) and 'Enemy' in ent.__class__.__name__ for ent in self.entity_list)
                    if enemy_count < self.MAX_ENEMIES:

                        self.entity_list.append(EntityFactory.get_entity('Enemy1'))
                        self.entity_list.append(EntityFactory.get_entity('Enemy2'))
                        self.entity_list.append(EntityFactory.get_entity('Enemy3'))

            self.level_text(14, f'Level 1 - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            #collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # printed text

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

        pass