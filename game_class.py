import pygame

TAMANHO_JANELA: tuple = (800, 600)


class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode(TAMANHO_JANELA)
        self.clock = pygame.time.Clock()
        self.game_state: bool = True

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = False
                return False

        return True

    def update_states(self):

        return True

    def draw_screen(self):
        self.tela.fill("purple")
        pygame.display.update()
        return True

    def game_loop(self):

        self.handle_event()
        self.update_states()
        self.draw_screen()

        return True

    def run(self):

        while self.game_state:
            self.game_loop()
            self.clock.tick(60)

        pygame.quit()
        exit(0)

