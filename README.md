# Route Optimizer (Simulated Annealing)

## Project Overview
This project is a Python-based command-line tool designed to solve a classic AI problem: the Traveling Salesperson Problem (TSP). It calculates the most efficient delivery route for a set of locations to minimize total travel distance. 

Instead of checking every single possible route (which takes too long) or using basic greedy algorithms (which get stuck in local minimums), this tool uses the **Simulated Annealing** algorithm. This allows the AI to occasionally accept "worse" routes early on to ensure it finds the true global best route by the end.

## Files Included
* `delivery_route.py`: The main Python script containing the AI logic and distance calculations.
* `locations.txt`: The dataset file containing the names and X/Y coordinates of the delivery stops.

## Prerequisites
* Python 3.x installed on your computer.
* No external libraries (like `pandas` or `numpy`) are required. It only uses Python's built-in `math` and `random` libraries.

## How to Run the Program

1. Open your terminal or command prompt.
2. Navigate to the folder where you saved these files.
3. Run the script by typing:
   `python delivery_route.py`
4. When the program asks for the file name, type:
   `locations.txt`
5. Press Enter. The AI will calculate thousands of routes and output the most optimized delivery path and the percentage of distance saved.

## AI Concepts Demonstrated
* **State-Space Search:** Navigating thousands of route combinations.
* **Heuristics:** Using Euclidean distance as the cost function to minimize.
* **Stochastic Optimization:** Using a temperature decay formula to escape local minimums and find the global optimum.

## Example Terminal Output
When you run the script, you will see an output similar to this:

Route Optimizer Tool
------------------------------
Enter file name (e.g., locations.txt): locations.txt

Calculating best route... please wait.

Optimization Finished.
Starting random distance: 412.35
AI optimized distance: 185.22

Best Route found:
Warehouse -> Stop_7 -> Stop_9 -> Stop_5 -> Stop_1 -> Stop_3 -> Stop_6 -> Stop_2 -> Stop_8 -> Stop_4 -> Warehouse

## Limitations and Future Improvements
* The current temperature decay rate is hardcoded to `0.995`. In a future update, this could be made dynamic based on the size of the dataset.
* The script currently uses Euclidean (straight-line) distance. To make this work for a real delivery truck, it would need to be connected to a mapping API (like Google Maps) to account for roads and traffic.
