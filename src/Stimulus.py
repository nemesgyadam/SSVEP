import pygame

class Stimulus:
    def __init__(self, cfg):
        self.cfg = cfg

        self.screen, self.WIDTH, self.HEIGHT, self.BLACK = self.init_game()
        self.image, self.black_surface = self.load_image(self.cfg['IMAGE_PATH'])
        self.flicker_rates = self.cfg['FLICKER_RATES']
        self.timers = [0 for _ in self.flicker_rates]
        self.visible = [True for _ in self.flicker_rates]
        self.running = True

    def init_game(self):
        pygame.init()
        infoObject = pygame.display.Info()
        WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
        BLACK = (0, 0, 0)
        return pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN), WIDTH, HEIGHT, BLACK

    def load_image(self, image_path):
        image = pygame.image.load(image_path).convert_alpha() 
        image_surface = pygame.Surface((self.WIDTH//4, self.HEIGHT//2), pygame.SRCALPHA)
        image_surface.blit(image, (0, 0))
        black_surface = pygame.Surface((self.WIDTH//4, self.HEIGHT//2), pygame.SRCALPHA)
        black_surface.fill((0, 0, 0))
        return image_surface, black_surface

    def loop(self):
        clock = pygame.time.Clock()
        self.screen.fill(self.BLACK)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                        self.running = False


            dt = clock.tick(60) / 1000
            for i, (rate, timer,  pos) in enumerate(zip(self.flicker_rates, self.timers,  self.cfg['IMAGE_POSITIONS'])):
                self.timers[i] += dt
                if timer >= 1/rate:
                    self.screen.blit(self.image if self.visible[i] else self.black_surface, (self.WIDTH*pos[0], self.HEIGHT*pos[1]))
                    self.visible[i] = not self.visible[i]
                    self.timers[i] = 0
            pygame.display.flip()
        pygame.quit()
