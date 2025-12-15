## Arcade Pong Game – Python Turtle

A feature-rich, arcade-style recreation of the classic Pong game built using Python and the Turtle graphics module. This version is enhanced with custom physics, dynamic difficulty scaling, and a full Game Over/Restart loop.
This project serves as a practical demonstration of Object-Oriented Programming (OOP), advanced state management, and external library integration (Pygame for sound).

# 🎮 Key Features & Technical Highlights
This game goes beyond a basic clone, implementing several features to demonstrate robust system design and a polished user experience:

 Object-Oriented Architecture (OOP): Built using separate, clean classes (Ball, Paddle, Scoreboard) for modularity and easy extension.

Dynamic Difficulty Scaling: Implements a custom speed curve where the ball accelerates after every score, ensuring the challenge increases continuously throughout the match.

 Precision UX / Guided Bounce: Features a state-based logic that guides the ball toward the opponent for the first few hits of a rally, guaranteeing fair starting rallies and improving the initial player experience.

 Paddle Dash / Boost: Added a dedicated key control to allow players to temporarily boost their paddle speed for difficult, last-second saves.

 Graceful Restart Loop: Implemented a bug-free "Press SPACE to Play/Restart" mechanism that clears the Game Over state, resets objects, and allows for infinite replayability.

Sound Integration: Uses the Pygame Mixer library for dedicated audio feedback (paddle hits, scoring, and a final win fanfare).

Arcade Aesthetics: Features a high-contrast Neon theme with dedicated goal lines and oversized scores.

# 📁 Project Structure
Pong-Game/
│
├── main.py        # Initializes game, manages keypresses, and runs the main loop
├── paddle.py      # Paddle class: handles movement, speed, and dash logic
├── ball.py        # Ball class: handles movement, physics, speed scaling, and bounce logic
├── scoreboard.py  # Scoreboard class: handles score display, updates, and Game Over messages
├── hit_paddle.wav # Sound asset (required for audio)
├── score_goal.wav # Sound asset (required for audio)
├── win_game.wav   # Sound asset (required for audio)
└── README.md


# 1.Requirements
The game requires Python 3 and the external pygame library for sound effects.
Install pygame via pip
pip install pygame

# 2. Run the Game
Navigate to the project directory in your terminal and execute:
python main.py
The game window will open, displaying the "Press SPACE to start" prompt.

# ⌨️ Controls

Action,Left Paddle,Right Paddle
Move Up,W,↑ (Up Arrow)
Move Down,S,↓ (Down Arrow)
Dash / Boost,D,→ (Right Arrow)
Start / Restart,SPACE,SPACE
