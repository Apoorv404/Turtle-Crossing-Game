# Turtle-Crossing-Game

A Python implementation of a road-crossing game using the Turtle graphics library. Guide your turtle safely across a busy road while avoiding cars.

## Features

- Player-controlled turtle that moves upward
- Randomly generated cars moving across the screen
- Increasing difficulty with each level
- Score tracking and level display
- Collision detection
- Game over state

## Implementation Details

### Components

- [`main.py`](main.py): Core game loop and initialization
- [`player.py`](player.py): Player turtle implementation
- [`car_manager.py`](car_manager.py): Car generation and movement
- [`scoreboard.py`](scoreboard.py): Score display and game over text

### Classes

- **Player**: Controls the turtle character
  - Movement mechanics
  - Position tracking
  - Finish line detection
  
- **CarManager**: Handles vehicle traffic
  - Random car generation
  - Car movement
  - Speed management
  - Multiple car colors
  
- **Scoreboard**: Manages game information
  - Level display
  - Game over message
  - Score tracking

## How to Play

1. Run `main.py`
2. Use the Up arrow key to move the turtle forward
3. Avoid colliding with cars
4. Reach the top of the screen to advance to the next level
5. Each level increases car speed
6. Game ends if you hit a car

## Technical Details

- Screen dimensions: 600x600 pixels
- Starting position: Bottom of screen
- Finish line: Top of screen
- Car generation: Random intervals
- Movement speed increases with each level
- Car colors: Red, Orange, Yellow, Green, Blue, Purple

## Dependencies

- Python 3.x
- turtle (built-in library)
- time (built-in library)
- random (built-in library)

## Implementation Constants

```python
# Player
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Display
FONT = ("Courier", 24, "normal")
```

## Game Mechanics

1. Player Movement:
   - Turtle moves up only
   - Fixed movement distance
   - Returns to start after crossing

2. Car Generation:
   - Random timing
   - Random y-position
   - Multiple colors
   - Increases speed each level

3. Level Progression:
   - Advance by reaching top
   - Cars speed up each level
   - Score updates automatically
