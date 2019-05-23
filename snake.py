import pygame
import random
import time

class SnakeGame:

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((400, 400))
        
        self.snake_body = [[200, 200], [200, 220], [200, 240]]
        self.snake_head = [200, 200]
        self.snake_direction = [0, -20]
        self.score = 0

    def start_game(self):
        green = (0, 255, 0)
        red = (255, 0, 0)
        black = (0, 0, 0)
        window_color = (200, 200, 200)
        playing = True
        direction = [0, -20]

        self.display.fill(window_color)
        pygame.display.update()
        clock = pygame.time.Clock()

        food_position = self.generate_food()
        score = 0

        while playing:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        direction = [-20, 0]
                    elif event.key == pygame.K_UP:
                        direction = [0, -20]
                    elif event.key == pygame.K_RIGHT:
                        direction = [20, 0]
                    elif event.key == pygame.K_DOWN:
                        direction = [0, 20]

            self.display.fill(window_color)
            self.draw_snake(red, green)
            self.draw_food(black, food_position)
            self.move_snake(direction)
            if self.snake_dead():
                playing = False

            if self.check_ate_food(food_position):
                score += 1
                food_position = self.generate_food()
            pygame.display.update()
            clock.tick(5)
        
        self.score = score

    def show_score(self):
        self.display.fill((230, 230, 230))
        score_text = pygame.font.SysFont("Arial", 30, italic=1, bold=2)
        text_display = score_text.render("Your score = " + str(self.score), True, (0, 0, 0))
        text_rect = text_display.get_rect()
        text_rect.center = (200, 200)
        self.display.blit(text_display, text_rect)
        pygame.display.update()
        time.sleep(2)
        self.display.fill((230, 230, 230))
        text_display = score_text.render("Closing now..", True, (0, 0, 0))
        text_rect = text_display.get_rect()
        text_rect.center = (200, 200)
        self.display.blit(text_display, text_rect)
        pygame.display.update()
        time.sleep(1)

    def add_vectors(self, v1, v2):
        return [v1[0]+v2[0], v1[1]+v2[1]]

    def snake_dead(self):
        if self.snake_head in self.snake_body[1:]:
            return True
        return self.snake_head[0] < 0 or self.snake_head[1] < 0 or self.snake_head[0] >= 400 or self.snake_head[1] >= 400

    def move_snake(self, direction):

        if self.add_vectors(self.snake_direction, direction) != [0, 0]:
            self.snake_direction = direction

        self.snake_head = self.add_vectors(self.snake_head, self.snake_direction)
        self.snake_body.insert(0,self.snake_head)
        self.snake_body.pop()

    def draw_snake(self, head_color, body_color):
        pygame.draw.rect(self.display, head_color, (self.snake_head[0], self.snake_head[1], 20, 20))
        for part in self.snake_body[1:]:
            pygame.draw.rect(self.display, body_color, (part[0], part[1], 20, 20))

    def generate_food(self):
        x = random.randint(0, 20) * 20
        y = random.randint(0, 20) * 20
        while (x, y) in zip(self.snake_body):
            x = random.randint(0, 20) * 20
            y = random.randint(0, 20) * 20
        return [x, y]
 
    def draw_food (self, food_color, food_position):
        pygame.draw.rect(self.display, food_color, (food_position[0], food_position[1], 20, 20))

    def check_ate_food(self, apple_position):
        if self.snake_head[0] == apple_position[0] and \
            self.snake_head[1] == apple_position[1]:
            self.snake_body += [[-20, -20]]
            return True
        return False


if __name__ == "__main__":
    snake = SnakeGame()
    snake.start_game()
    snake.show_score()

    pygame.quit()

