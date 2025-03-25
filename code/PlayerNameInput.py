import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, COLOR_PINK


def input_player_name(window, score):
    """
    Tela para input do nome do jogador antes de salvar o score
    """
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('palatinolinotype', 40)
    input_font = pygame.font.SysFont('palatinolinotype', 60)

    # Background da tela de input
    background = pygame.image.load('./asset/menuCE.png').convert_alpha()
    background_rect = background.get_rect(left=0, top=0)

    # Variáveis para input do nome
    player_name = ""
    input_active = True

    while input_active:
        window.blit(background, background_rect)

        # Renderizar instruções
        title = font.render("Digite seu nome (3 caracteres)", True, COLOR_PINK)
        title_rect = title.get_rect(center=(WIN_WIDTH / 2, 100))
        window.blit(title, title_rect)

        # Renderizar input do nome
        name_surface = input_font.render(player_name, True, COLOR_WHITE)
        name_rect = name_surface.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        window.blit(name_surface, name_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(player_name) > 0:
                    # Salvar score com o nome
                    return player_name

                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]

                # Permitir apenas letras maiúsculas e limitar a 3 caracteres
                if event.unicode.isalpha() and len(player_name) < 3:
                    player_name += event.unicode.upper()

        clock.tick(30)

    return player_name