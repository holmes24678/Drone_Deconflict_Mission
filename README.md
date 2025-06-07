# Drone Mission Deconfliction and Visualization

## Overview

This project provides a modular Python solution to simulate and detect conflicts in multiple drone trajectories. It performs spatial and temporal checks to identify potential collisions between drones following their predefined paths.

- **main.py**: Entry point that loads missions, checks for conflicts, and visualizes results.
- **deconflict.py**: Contains logic for loading missions and performing conflict detection.
- **visualization.py**: Visualizes drone trajectories and animates the primary drone's mission.
- **collide.json**: JSON file containing mission waypoints and paths for the primary and other drones.

## Features

- Detects conflicts based on spatial distance and timing between drones.
- Visualizes 3D trajectories of multiple drones.
- Animates the primary drone’s path.
- Modular and easy to extend.

## Requirements

- Python 3.7+
- `matplotlib`
- `numpy`

Install dependencies with:

```bash
pip install matplotlib numpy
 ```
## Execution

Make sure your JSON file (`collide.json`) and (`mission.json`) is present in the project directory.

Run the main script using:

```bash
python main.py
```

## Example Output

- If conflicts are detected, the terminal will show something like:

⚠️ **Conflict Detected!**  
**Time:** 12.5s | **Location:** [15.3, 20.1, 5.0] | **With:** Drone 2 | **Distance:** 1.45  
**Time:** 15.0s | **Location:** [18.7, 22.3, 6.0] | **With:** Drone 3 | **Distance:** 1.30  

- If no conflicts are found:

✅ **Mission is clear of conflicts.**

## Visualization

After the console output, a 3D plot window will open showing:

- The primary drone’s mission path, animated over time.
- Other drones’ trajectories in distinct colors.
- Red “X” marks at conflict points, if any.

You can interact with the 3D plot (rotate, zoom) to better analyze drone paths.

Close the plot window to terminate the program.
