# Capture the Flag Agents

A repository exploring consepts within the Intelligent Agents and Multi-Agent Systems branch of Artificial Intelligence in a 2D game environment.  

## Current Project Objectives
Create a 2D grid environment of and implement a Simple Reflex Agent to navigate the grid and achieve a simple objective, capture a flag.

## Project Plan
### Environment
- 2D 
- 5X5 grid 
- Consists of agents, flags, bases, and obsitcals. 
### Agent Sensors
- View the occupied space; one space in front, to the sides, and the front diagonals.
### Agent Actuators
- Move forward or backward one space.
- Rotate 90 degrees left or right.
- Interact with the cell they occupy  
- Agents can communicate to other agents at any time.
- Agents know where flags are at all times.
### Execution Loop
- The loop is executed until the simulation is ended.
- In each iteration:
	1. All agents perceives the environment.
	2. Agents chose an action to perform.
	3. Agents the execute their actions.
	4. The environment is then updated.

## Game Rules
- Only one agent can ocupy a space at once.
- Agents can "tag" other agents infront to reset a flag they're holding.