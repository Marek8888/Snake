import pygame

import sys

from settings import Settings

from body_movement import Body


class Game:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.score = 0
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.direction = {
            'up': False,
            'down': False,
            'right': True,
            'left': False,
        }
        self.last_key = 'right'
        self.settings.clock = pygame.time.Clock()
        # Create subclass od Body
        self.body = Body(self)

    def only_one_direction(self, direction):
        """Allow only vertical and horizontal movement at the time"""
        for direct in self.direction:
            self.direction[direct] = False
        self.direction[direction] = True

    def snake_head_movement(self):
        if self.direction['up']:
            self.body.snake_position[1] -= self.settings.snake_speed
        if self.direction['down']:
            self.body.snake_position[1] += self.settings.snake_speed
        if self.direction['left']:
            self.body.snake_position[0] -= self.settings.snake_speed
        if self.direction['right']:
            self.body.snake_position[0] += self.settings.snake_speed

    def _check_key_downs(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print(self.body.score)
                sys.exit()

            if event.key == pygame.K_DOWN and self.last_key != 'up':
                self.direction['down'] = True
                self.last_key = 'down'
                self.only_one_direction('down')
            if event.key == pygame.K_UP and self.last_key != 'down':
                self.last_key = 'up'
                self.direction['up'] = True
                self.only_one_direction('up')
            if event.key == pygame.K_LEFT and self.last_key != 'right':
                self.last_key = 'left'
                self.direction['left'] = True
                self.only_one_direction('left')
            if event.key == pygame.K_RIGHT and self.last_key != 'left':
                self.last_key = 'right'
                self.direction['right'] = True
                self.only_one_direction('right')

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self._check_key_downs(event)
            self.screen.fill(self.settings.screen_color)
            self.settings.get_lines_printed(self)
            self.body.draw_components()
            self.body.check_boundries()
            self.snake_head_movement()
            self.body.snake_body_movement()
            pygame.display.flip()
            self.body.body_collision()
            # set FPS
            self.settings.clock.tick(12)


if __name__ == '__main__':
    snake = Game()
    snake.run_game()