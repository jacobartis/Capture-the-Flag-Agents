# Painting Agents

A repository exploring consepts within the Intelligent Agents and Multi-Agent Systems branch of Artificial Intelligence.  

## Current Project Objectives
Create a 2D grid environment of and implement a Simple Reflex Agent to navigate the grid and achieve a simple objective.

## Project Plan
### Environment
- 2D 
- 5X5 grid 
- Consists of white or blue squares. 
- The agent starts at coordinates 0,0 in the top left for the grid.
### Agent Sensors
- View the occupied space; one space in front, to the sides, and the front diagonals.
### Agent Actuators
- Move forward or backward one space.
- Rotate 90 degrees left or right.
- Change the colour of the occupied to the Agents colour.  
### Execution Loop
- The loop is executed until the simulation is ended.
- In each iteration:
	1. All agents perceives the environment.
	2. Agents chose an action to perform.
	3. Agents the execute their actions.
	4. The environment is then updated.