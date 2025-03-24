import pygame
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.original_surf = self.surf.copy()  # Guarda a imagem original
        self.is_hurt = False  # Estado de dano
        self.hurt_timer = 0  # Temporizador de dano

        # Carregar som de miado
        self.meow_sound = pygame.mixer.Sound('./asset/meow.mp3')  # Caminho do som
        self.meow_sound.set_volume(0.2)  # Ajustar volume se necessário

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def take_damage(self):
        """Ativado quando o jogador sofre dano."""
        if not self.is_hurt:  # Evita sobreposição de animação
            self.is_hurt = True
            self.hurt_timer = pygame.time.get_ticks()  # Marca o tempo inicial
            self.surf.fill((255, 0, 0), special_flags=pygame.BLEND_MULT)  # Fica vermelho
            self.meow_sound.play()  # Toca o som

    def update(self):
        """Reseta a cor do jogador após um tempo."""
        if self.is_hurt:
            if pygame.time.get_ticks() - self.hurt_timer > 300:  # 300ms de dano
                self.is_hurt = False
                self.surf = self.original_surf.copy()  # Volta à imagem original