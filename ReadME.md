# Nutritionix and Sheety Workout Tracker

### Introduction

This Python script serves as a workout tracker, utilizing the Nutritionix API for exercise information and the Sheety API for storing and retrieving workout data.
Prerequisites

Before using the script, ensure you have the following:

    - Nutritionix API Credentials: Obtain your Nutritionix ID and API Key.
    - Sheety API Credentials: Ensure you have necessary credentials for the Sheety API.
    - Python Environment: The script is written in Python. Make sure you have Python installed.

## Usage

    Pre-RUN:
        Please Adapt Create /Nutritionix/creds.py
        Add your info for more accurate results:

            USER_INFO = {
                "gender": "male",
                "weight_kg": "75",
                "height_cm": "172",
                "age": "29",
            }
      

    Nutritionix API Setup:
        Run the script.
        When prompted, enter your Nutritionix ID and API Key.

    Get Exercise Information:
        Enter the exercise details when prompted.
        The script will retrieve information such as exercise name, calories burned, and duration using the Nutritionix API.

    Sheety Integration:
        The workout details are then formatted and stored in a dictionary.
        The SheetyApi class is used to interact with the Sheety API.
        You'll be prompted to print the latest workout information.
        If desired, add new workout data, which will be stored in a Sheety database.

## Code Structure

    Datetime Module: Utilized for timestamping workout entries.
    NutritionixSetup Class: Handles interaction with the Nutritionix API.
    SheetyApi Class: Manages communication with the Sheety API.

## Script Execution

    Run the script.
    Enter Nutritionix API credentials.
    Input exercise details.
    Review or add workout data using the Sheety API.

## Improvements

Feel free to enhance the script by adding more features, error handling, or additional data points.

Note: Make sure to keep your API credentials secure and not share them publicly.

Enjoy tracking your workouts!