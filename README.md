# Ping-Pong-Ball-Game

# Python Ping Pong Game

A real-time Ping Pong game built using **Python** and **Pygame**. This project includes ball-paddle collision detection, scoring, sound effects, and a replay menu with configurable match lengths.

---

## Features

- **Real-time gameplay** with smooth paddle and ball movement.
- **Collision detection** to prevent the ball from passing through paddles.
- **Scoring system**: first player to reach the winning score wins.
- **Game over screen**: displays the winner and replay options.
- **Replay menu**:
  - Best of 3 (first to 2)
  - Best of 5 (first to 3)
  - Best of 7 (first to 4)
  - Exit
- **Sound effects**:
  - Paddle hit
  - Wall bounce
  - Score
- **AI opponent** that tracks the ball automatically.

---

## Installation

1. **Clone the repository**:

```bash
git clone <repository-url>
cd ping-pong

ping-pong/
├── main.py              # Entry point
├── game/
│   ├── game_engine.py   # Handles game logic, collision, scoring, game over
│   ├── paddle.py        # Paddle class (player and AI)
│   └── ball.py          # Ball class with movement and collision
├── assets/              # Sound files
│   ├── paddle_hit.mp3
│   ├── wall_bounce.mp3
│   └── score.wav
└── README.md
