# The Smashers
A Major Mathematics group project with micro:bit(TM) und Maqueen(TM).

The Smashers is a project to produce a fun police-and-thief game. The two Maqueens are best played on the floor of a small empty room with lots of obstacles.

## Installation
### Requirements
* 3x micro:bits
* 2x Maqueens

### Online
1. Open https://makecode.microbit.org/ on a Chromium-based browser
2. Include the extension DFRobot_MaqueenPlus_v20
3. Flash `basher.py` to two micro:bits
4. Insert one of those `basher.py` micro:bit into a Maqueen
5. Flash `dasher.py` to the third micro:bit
6. Insert the `dasher.py`-flashed micro:bit into a Maqueen

## The Basher
The Basher is a police robot. Its main task is to catch the Dasher. The only possibility to catch the Dasher is to move it to the corner, where the Dasher will have not chance to run away. The Basher is controlled by human, so the player can calculate and implement the best tactic how the Dasher can be caught.

The Basher has been configured to be controlled with one remote micro:bit. Controls are like instruments: they are cumbersome at first but become easier over time. Press `a + b` to start/stop. If you press `a + b` quickly, you'll go in reverse. While driving forward, press `a` to make a left turn, `b` to make a right turn.

## The Dasher
The Dasher is a thief robot that is trying to run away from the Basher. It is controlled, so it cannot be controlled by a player. The directions that it chooses are random and independet. It is able to see that barriers and to avoid them successfully.
