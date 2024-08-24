import pygame


class Game:
    # constantes e configurações
    RESOLUCAO: tuple = (800, 600)
    CENTRO_TELA: tuple = (RESOLUCAO[0] / 2, RESOLUCAO[1] / 2)
    PARADO, CIMA, BAIXO, ESQUERDA, DIREITA = 0, 1, 2, 3, 4

    # atributos: variáveis
    delta_time: float

    # atributos: objetos
    jogador: dict = \
        {
            'sprite_surface': None,
            'posicao': [0, 0],
            'direcao': {'PARADO': False, 'CIMA': False, 'BAIXO': False, 'ESQUERDA': False, 'DIREITA': False},
            'vivo': True,
            'movimento': True
        }

    # construtor da classe
    def __init__(self):
        pygame.init()
        self.jogador['posicao'] = list(self.CENTRO_TELA)

        self.tela = pygame.display.set_mode(self.RESOLUCAO)
        self.clock = pygame.time.Clock()
        self.game_state: bool = True

    # método para lidar com o controle de eventos do jogo
    def handle_event(self):
        # verifica quais eventos ocorreram
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.game_state = False
                    return False
                case pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_state = False
                        return False

        # verifica quais teclas estão pressionadas
        teclas_pressionadas = pygame.key.get_pressed()

        if teclas_pressionadas[pygame.K_UP] | teclas_pressionadas[pygame.K_w] and not self.jogador['movimento']:
            self.jogador['movimento'] = True
            self.jogador['direcao']['PARADO'] = False
            self.jogador['direcao']['CIMA'] = True

        if teclas_pressionadas[pygame.K_DOWN] | teclas_pressionadas[pygame.K_s] and not self.jogador['movimento']:

            self.jogador['movimento'] = True
            self.jogador['direcao']['PARADO'] = False
            self.jogador['direcao']['BAIXO'] = True

        if teclas_pressionadas[pygame.K_LEFT] | teclas_pressionadas[pygame.K_a] and not self.jogador['movimento']:

            self.jogador['movimento'] = True
            self.jogador['direcao']['PARADO'] = False
            self.jogador['direcao']['ESQUERDA'] = True

        if teclas_pressionadas[pygame.K_RIGHT] | teclas_pressionadas[pygame.K_d] and not self.jogador['movimento']:

            self.jogador['movimento'] = True
            self.jogador['direcao']['PARADO'] = False
            self.jogador['direcao']['DIREITA'] = True

        if teclas_pressionadas[pygame.K_ESCAPE]:
            self.game_state = False
            return False
        return True

    # método para atualizar os dados dos objetos do jogo
    def update_states(self):
        # verifica se jogador está em movimento
        if not self.jogador['direcao']['PARADO']:
            if self.jogador['direcao']['CIMA']:
                self.jogador['posicao'][1] -= 3
                self.jogador['direcao']['CIMA'] = False
            if self.jogador['direcao']['BAIXO']:
                self.jogador['posicao'][1] += 3
                self.jogador['direcao']['BAIXO'] = False
            if self.jogador['direcao']['ESQUERDA']:
                self.jogador['posicao'][0] -= 3
                self.jogador['direcao']['ESQUERDA'] = False
            if self.jogador['direcao']['DIREITA']:
                self.jogador['posicao'][0] += 3
                self.jogador['direcao']['DIREITA'] = False

            self.jogador['direcao']['PARADO'] = True
            self.jogador['movimento'] = False


        return True

    # método para desenhar a tela do jogo
    def draw_screen(self):
        # limpa tela
        self.tela.fill("white")

        # desenha personagem
        pygame.draw.circle(self.tela, "red", self.jogador['posicao'], 20)

        # atualiza tela
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

            # limits FPS to 60
            # delta time in seconds since last frame, used for frame rate independent physics.
            self.delta_time = self.clock.tick(60) / 1000

        pygame.quit()
        exit(0)
