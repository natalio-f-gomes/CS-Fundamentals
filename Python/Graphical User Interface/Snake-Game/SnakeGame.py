import csv

import pygame
import time
import random


class SnakeGame:
    def __init__(self):
    # Initialize Pygame
        pygame.init()

        # Define the game window size
        self.window_width = 800
        self.window_height = 600

        # Define the colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)


        # Create the game window
        self.game_display = pygame.display.set_mode((self.window_width, self.window_height))



        # Set the game window title
        pygame.display.set_caption('Snake Game')

        # Define the game's clock
        self.clock = pygame.time.Clock()

        # Define the Snake's size and speed
        self.snake_block_size = 10
        self.snake_speed = 15

        # Create the font
        self.font_style = pygame.font.SysFont("Arial", 50)

# Define the function to display the message on the screen
    def score_message(self,msg, color):
        message_display = self.font_style.render(msg, True, color)
        self.game_display.blit(message_display, [0, 0])



    def handle_score(self,score):
        with open("bestScore.csv", 'r') as file:
            file_r = csv.reader(file)
            best_score = max([int(row[0]) for row in file_r])
            if score > best_score:
                with open("bestScore.csv", 'w', newline='') as file:
                    file_w = csv.writer(file)
                    file_w.writerow([score])
            return best_score

    def best_score_message(self,best_score):


        message_display = self.font_style.render(f"Best Score: {best_score} ", True, self.black)
        self.game_display.blit(message_display, [350, 0])

    def lose_message(self,msg, color):
        message_display = self.font_style.render(msg, True, color)
        self.game_display.blit(message_display, [self.window_width/2-100,self.window_height/2-100])

    # Define the main function for the game
    def game_loop(self):

        # Define the Snake's initial position
        snake_position = [self.window_width/2, self.window_height/2]

        # Define the Snake's body
        snake_body = [[snake_position[0], snake_position[1]],
                      [snake_position[0]- self.snake_block_size, snake_position[1]],
                      [snake_position[0]-(2* self.snake_block_size), snake_position[1]]]

        # Define the initial food position
        food_position = [random.randrange(0, self.window_width// self.snake_block_size)* self.snake_block_size,
                         random.randrange(0, self.window_height//self.snake_block_size)*self.snake_block_size]

        # Define the initial direction of the Snake
        direction = 'right'
        change_direction = direction

        # Set the initial game score to 0
        score = 0

        # Start the game loop
        while True:

            # Handle the events in the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # If the user closes the window, terminate the program
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        change_direction = 'left'
                    elif event.key == pygame.K_RIGHT:
                        change_direction = 'right'
                    elif event.key == pygame.K_UP:
                        change_direction = 'up'
                    elif event.key == pygame.K_DOWN:
                        change_direction = 'down'

            # Change the direction of the Snake
            if change_direction == 'left' and direction != 'right':
                direction = 'left'
            elif change_direction == 'right' and direction != 'left':
                direction = 'right'
            elif change_direction == 'up' and direction != 'down':
                direction = 'up'
            elif change_direction == 'down' and direction != 'up':
                direction = 'down'

            # Move the Snake
            if direction == 'left':
                snake_position[0] -= self.snake_block_size
            elif direction == 'right':
                snake_position[0] += self.snake_block_size
            elif direction == 'up':
                snake_position[1] -= self.snake_block_size
            elif direction == 'down':
                snake_position[1] += self.snake_block_size

            # If the Snake reaches the border, end the game
            if snake_position[0] >= self.window_width or snake_position[0] < 0 or snake_position[1] >= self.window_height or snake_position[1] < 0:
                self.lose_message('You lost!', self.red)
                pygame.display.update()
                time.sleep(2)
                self.game_loop()

            # Update the Snake's body
            snake_head = [snake_position[0], snake_position[1]]
            snake_body.insert(0, snake_head)
            if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
                food_position = [random.randrange(0, self.window_width//self.snake_block_size)*self.snake_block_size,
                                 random.randrange(0, self.window_height//self.snake_block_size)*self.snake_block_size]
                score += 10
            else:
                snake_body.pop()

            # Draw the game objects on the screen
            self.game_display.fill(self.white)
            for block in snake_body:
                pygame.draw.rect(self.game_display, self.green, [block[0], block[1], self.snake_block_size, self.snake_block_size])
            pygame.draw.rect(self.game_display, self.red, [food_position[0], food_position[1], self.snake_block_size, self.snake_block_size])

            # Update the game score
            self.score_message('Score: ' + str(score), self.black)


            self.best_score_message(self.handle_score(score))



            # Update the game window
            pygame.display.update()

            # Check if the Snake hits itself
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    self.lose_message('You lost!', self.red)
                    pygame.display.update()
                    time.sleep(2)
                    self.game_loop()

            # Set the game's frame rate
            self.clock.tick(self.snake_speed)
        pygame.display.update()
        # Quit Pygame and Python
        pygame.quit()
        quit()


