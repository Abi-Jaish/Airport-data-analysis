European Airport Data Analysis

This project is a comprehensive Python application developed to analyze 12-hour datasets of European airport departures. The program automates the process of loading large CSV datasets, performing complex statistical calculations, and providing visual feedback to help survey groups make informed decisions on air traffic.

Key Features

1. Input validation
  Implemented strict validation for IATA airport codes (e.g., LHR, CDG, AMS).
  Integrated year-range validation (2000–2025) with error handling for data types and out-of-range values.
  Case-insensitive input handling to improve user experience.

2. Data Processing and Analytics
   Total flight counts and terminal-specific data.
   Airline-specific performance (e.g., Air France delay percentages).
   Weather analysis (flights departing below 15°C and rain frequency).
   Average departure rates and identifying least common destinations.

3. Data Persistence and Looping
   Developed a logging system that appends results to `results.txt` without overwriting previous data.
   Built a program loop allowing users to analyze multiple datasets in a single session.

4. Histogram
   Created a dynamic, auto-scaling horizontal histogram using the `graphics.py` module.
   The visualization includes labeled axes, hourly flight counts, and airline-specific titles.

Note: This project was developed as a graded assessment for the Software Development I (4COSC006C) module at the University of Westminster. It is shared here for portfolio purposes to demonstrate proficiency in Python, data processing, and graphical visualization.
