import pygame


class Settings:
    def __init__(self):
        self.snake_speed = 23
        self.screen_width = 460
        self.screen_height = 460
        self.screen_color = (0, 0, 0)
        self.line_lenght_x = self.screen_width
        self.line_lenght_y = self.screen_height
        self.line_color = (60,60,60)
        self.line_width = 1
        self.vertical = self.screen_width // 23
        self.horizontal = self.screen_height // 23
        self.horizontal_lines = []
        self.vertical_lines = []
        self.clock = pygame.time.Clock()

    def _get_horizontal_lines(self):
        self.horizontal_lines = []
        for i in range(self.vertical):
            rect = pygame.Rect(i*23, 0, self.line_width, self.line_lenght_y)
            self.horizontal_lines.append(rect)

    def _get_vertical_lines(self):
        self.vertical_lines = []
        for i in range(self.horizontal):
            rect = pygame.Rect(0, i*23, self.line_lenght_x, self.line_width)
            self.vertical_lines.append(rect)

    def draw_horizontal_lines(self,sneaky):
        self._get_horizontal_lines()
        for rect in self.horizontal_lines:
            pygame.draw.rect(sneaky.screen, self.line_color, rect)

    def draw_vertical_lines(self, sneaky):
        self._get_vertical_lines()
        for rect in self.vertical_lines:
            pygame.draw.rect(sneaky.screen, self.line_color, rect)

    def get_lines_printed(self, sneaky):
        """Print grid"""
        self.draw_horizontal_lines(sneaky)
        self.draw_vertical_lines(sneaky)