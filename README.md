# PONG GAME
#### Video Demo: 
#### Description: This is a simple Pong Game made using Python.

## Overview
This project is a simple yet engaging implementation of the classic Pong game using Python and the Turtle graphics module. The game follows the traditional mechanics of Pong, where two players control paddles to hit a bouncing ball and prevent it from crossing their respective sides. The game runs in a graphical window, tracks the score, and increases difficulty dynamically as the ball's speed adjusts upon paddle hits.

## Files and Their Functions
The project consists of four main files:

### 1. `main.py`
This is the core of the game, responsible for initializing the game environment, handling player controls, and implementing the game loop.
- Sets up the game screen (800x600, black background, titled "Pong").
- Creates game objects: two paddles, the ball, and the scoreboard.
- Listens for keyboard inputs to control paddle movements.
- Manages game mechanics, such as ball movement, paddle collision detection, scoring, and game speed adjustments.

### 2. `paddle.py`
This file defines the `Paddle` class, which represents the player-controlled paddles.
- Each paddle is a white rectangular object positioned on either side of the screen.
- The class has methods `up()` and `down()` to move the paddle up and down.
- Uses the Turtle graphics module to render the paddle and handle movement.

### 3. `ball.py`
The `Ball` class manages the behavior of the Pong ball.
- The ball is initialized as a white circle with a random starting angle.
- The `move()` method controls its forward movement.
- `bounce_wall()` changes the ball’s direction when it hits the top or bottom walls.
- `bounce_paddle()` changes the ball’s direction when it collides with a paddle and increases speed.
- `reset_position()` resets the ball to the center when a player scores, choosing a new random direction.

### 4. `scoreboard.py`
This file contains the `Scoreboard` class, responsible for displaying and updating the players' scores.
- Maintains `l_score` and `r_score` variables for the left and right players.
- Uses the `update_scoreboard()` method to update the score display whenever a player scores a point.
- Includes methods `l_point()` and `r_point()` to increase scores when the ball crosses the screen boundaries.

## Design Decisions
Several design choices were made to ensure smooth gameplay:

### 1. **Ball Movement and Speed Adjustments**
- The ball starts with a random heading to create variation in gameplay.
- When the ball hits a paddle, its speed increases slightly, making the game progressively harder.

### 2. **Collision Mechanics**
- Paddle collision detection is based on the ball's distance from the paddle and its X-coordinate range.
- Wall collisions result in a vertical bounce, preserving the physics of a Pong game.

### 3. **User Input Handling**
- The game listens for key presses (`W/S` for the left paddle, `Up/Down` for the right paddle).
- `onkeypress()` ensures smooth movement without holding down keys continuously.

### 4. **Game Loop and Rendering**
- The `while` loop continuously updates the screen and moves the ball based on its speed.
- `screen.tracer(0)` ensures smooth frame updates without excessive rendering lag.
- A slight delay (`time.sleep(ball.move_speed)`) keeps the game responsive while controlling speed changes dynamically.
