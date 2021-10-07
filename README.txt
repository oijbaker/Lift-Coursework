Lift Control System:

The zip file contains four other folders. These are:
- Baseline Simulation
- Baseline System
- Improved Simulation
- Improved System

Both the baseline and improved system folders contain 4 python files. When run, these files will run a single run
through of the lift system. As a user, you will be asked to enter 3 numbers. The number of floors, the number of
lifts, and the number of people. These must be positive integers greater than 0. If the numbers are too big (depending 
on screen size), the floors, lifts or people may not fit on  the screen. However, the system will still run as intended. 
These programs will produce a graph at the end of the simulation, which shows all the times the system has run. These 
are stored in 'waittimelog.txt'. The graph will only show the entries where the number of lifts is the same as the number
used in the simulation that has just been run. For example, if I ran a simulation using 4 lifts, then only the previous
simulations with 4 lifts will show on the graph.

The baseline and improved simulation folders also contain 4 python files. When these are run, they simulate a number of 
simulations run over a range of values. You will be asked to enter a number of lifts. This must be between 1 and 10.
The system runs best at around 6 lifts. These programs take some time to run (about 20-30 seconds), and will produce a
3D graph which shows all of the simulations run. (The file is cleared before the simulation file is run, so the results
are new every time the file is run). 

To run the files, run 'main.py' in the respective file. For example, to run the Baseline Simulation, go to the file
'Baseline Simulation' and run 'main.py'.