"""
Entry point for the AI itinerary planner application.

Main Functionality:
- Collects user input from the terminal (e.g., start location, tasks, time budget).
- Calls the `plan_route` function to generate an optimized route.
- Displays the route and total time spent in a readable format.

Usage:
Run this script in the terminal to start the application:
$ python main.py
"""

import json
import os
import time  # To generate timestamp for filenames
# from planner.routes import plan_route
# from planner.utils import format_route_output

def save_user_data(user_data):
    """Saves the collected user data as a JSON file in the data/ folder."""
    # Ensure the data folder exists
    os.makedirs("data", exist_ok=True)

    # Generate a timestamped filename
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"data/user_input_{timestamp}.json"

    # Save the data as a JSON file
    with open(filename, 'w') as f:
        json.dump(user_data, f, indent=4)

    print(f"User input saved to {filename}")

def collect_user_inputs():
    """Collects user inputs from the terminal and returns them as a dictionary."""
    print("Welcome to the AI Itinerary Planner!")
    
    start_location = input("Enter your starting location (e.g., 'Shanghai Tower'): ").strip()

    tasks = []
    while True:
        task_name = input("\nEnter the task name (e.g., 'Buy matcha cake'): ").strip()
        fixed_location = input("Enter the location (if fixed), or leave empty: ").strip()
        is_fixed = bool(fixed_location)

        task = {"name": task_name, "location": fixed_location if is_fixed else None, "is_fixed": is_fixed}
        tasks.append(task)

        more_tasks = input("Add another task? (y/n): ").strip().lower()
        if more_tasks != 'y':
            break

    while True:
        try:
            time_budget = int(input("\nEnter your total time budget (in minutes): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    travel_mode = input("Enter preferred travel mode (walking, driving, bicycling, transit): ").strip().lower()

    user_data = {
        "start_location": start_location,
        "tasks": tasks,
        "time_budget": time_budget,
        "travel_mode": travel_mode
    }

    return user_data

def main():
    """Main function to collect inputs, plan the route, and store data."""
    user_data = collect_user_inputs()  # Gather inputs from the user

    # Save the input data to the data/ folder
    save_user_data(user_data)

    # Plan the route and display the output
    # route_plan = plan_route(user_data)
    print("\nYour optimized itinerary:")
    # print(format_route_output(route_plan))

if __name__ == "__main__":
    main()


