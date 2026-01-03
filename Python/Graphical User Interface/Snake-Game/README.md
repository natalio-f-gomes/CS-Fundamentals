Snake Game 
<p align="center">
  <img width="912" alt="Screenshot 2023-04-30 at 3 22 36 PM" src="https://user-images.githubusercontent.com/116610989/235372503-3c9e1d65-a2c8-402a-a3a4-93ea1d4b9d4f.png">
</p>
Description

This is a classic Snake Game built using the Pygame library in Python. The game consists of a snake moving around the screen eating food and growing in length. The goal of the game is to keep the snake alive and grow it as long as possible.

Requirements

To run the game, you need to have Python3 and Pygame installed in your system. You can install Pygame by running the following command in your terminal:

Copy code
pip install pygame
Installation

You can clone this repository by running the following command in your terminal:

bash
Copy code
git clone https://github.com/Nataliof22/YOUR-REPOSITORY
Usage

To start the game, navigate to the cloned repository folder and run the following command in your terminal:

python main.py or python3 main.py
Once you run the command, the game window will appear, and you can start playing the game.

How to Play

Use the arrow keys to move the snake in the desired direction.
Eat as many food pieces as possible to score points and grow the snake.
If the snake hits the border or its own body, the game will end.
The score will be displayed on the top left corner of the screen.
The best score achieved so far will be displayed on the top middle part of the screen.
Once the game is over, the game will restart automatically.
Game Controls

Key	Function
←	Move the snake left
→	Move the snake right
↑	Move the snake up
↓	Move the snake down
Game Features

The Snake Game has the following features:

A score system that increments by 10 points when the snake eats food.
A high score system that saves the best score achieved so far.
A game over message displayed when the snake dies.
The game window closes when the user clicks on the close button.
The game restarts automatically when the snake dies.
Code Explanation

The Snake Game code is written in Python and uses the Pygame library to handle the graphics and events in the game.

The code initializes Pygame and defines the game window size and colors. It also sets the Snake's size and speed and creates the game font.

The game loop is started, and the Snake's initial position, body, food position, and direction are defined. The loop handles the events in the game, such as moving the Snake, changing its direction, and updating its body.

If the Snake reaches the border or hits its body, the game is over. The score is displayed on the screen, and the best score achieved so far is saved.
<p align="center">
  <img width="912" alt="Screenshot 2023-04-30 at 3 22 52 PM" src="https://user-images.githubusercontent.com/116610989/235372512-2cc8e954-61da-4258-a7d7-1f26ec435102.png">
</p>
