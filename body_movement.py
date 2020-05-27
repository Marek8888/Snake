import sys

import pygame


import random


class Body:
    def __init__(self, sneaky):
        self.screen = sneaky.screen
        self.settings = sneaky.settings
        self.snake_position = [92, 46]
        self.snake_body = [[92, 46], [92 - 23, 46], [92 - (2 * 23), 46]]
        self.score = sneaky.score
        self.food_range = []
        for i in range(0, self.settings.screen_height):
            if i % self.settings.snake_speed == 0:
                self.food_range.append(i)
        self.food_position = [random.choice(self.food_range), random.choice(self.food_range)]
        self.food_visible = False

    def body_collision(self):
        for i in range(2, len(self.snake_body)):
            if self.snake_position == self.snake_body[i]:
                print(self.score)
                sys.exit()

    def new_food(self):
        """Assign food in a random position that fits grid"""
        self.food_position = [random.choice(self.food_range), random.choice(self.food_range)]
        self.food_visible = True

    def _draw_food(self):
        if not self.food_visible:
            image = pygame.image.load('images/food.bmp')
            rect = image.get_rect()
            rect.x = self.food_position[0]
            rect.y = self.food_position[1]
            self.screen.blit(image, rect)

    def _draw_snake(self):
        for elements in self.snake_body:
            image = pygame.image.load('images/head.bmp')
            rect = image.get_rect()
            rect.x = elements[0]
            rect.y = elements[1]
            self.screen.blit(image, rect)

    def draw_components(self):
        """Draw snake and food"""
        self._draw_snake()
        self._draw_food()

    def snake_body_movement(self):
        self.snake_body.insert(0, list(self.snake_position))
        if self.snake_position[0] == self.food_position[0] and self.snake_position[1] == self.food_position[1]:
            self.new_food()
            self.score += 1
            self.food_visible = False
        else:
            self.snake_body.pop()

    def check_boundries(self):
        if self.snake_position[0] > self.settings.screen_width:
            self.snake_position[0] = -self.settings.snake_speed
        elif self.snake_position[0] < 0:
            self.snake_position[0] = self.settings.screen_width
        elif self.snake_position[1] < 0:
            self.snake_position[1] = self.settings.screen_height
        elif self.snake_position[1] > self.settings.screen_height:
            self.snake_position[1] = -self.settings.snake_speed
