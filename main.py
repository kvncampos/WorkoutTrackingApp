import datetime
from Nutritionix.Nutritionix import NutritionixSetup
import os
from Nutritionix.creds import NUTRITIONIX_ID, NUTRITIONIX_API_KEY, USER_INFO
from Sheety.sheety_api import SheetyApi


# ------------------------------------------------------------------------------------------------------------
# os.environ['nutritionix_id'] = str(input("What is the Nutrionix ID? "))
# os.environ['nutritionix_api_key'] = str(input("What is the Nutrionix API Key? "))
#
# NUTRITIONIX_ID = os.environ['nutritionix_id']
# NUTRITIONIX_API_KEY = os.environ['nutritionix_api_key']

# ------------------------------ GET EXERCISE INFORMATION ---------------------------------------------------
exercise_call = NutritionixSetup(id=NUTRITIONIX_ID, api_key=NUTRITIONIX_API_KEY, user_info=USER_INFO)

new_data = input("What Exercise did you do? Ex: Heavy Weights 60 min\n")
# workout = exercise_call.post_nl_exercise('heavy weights 60 min')
workout = exercise_call.post_nl_exercise(new_data)
exercise = workout['name']
calories = workout['calories_burned']
duration = workout['duration']


# ------------------------------ SHEETY TEMPLATE ---------------------------------------------------
now = datetime.datetime.now()
formatted_now = now.strftime('%Y/%m/%d')
formatted_time = now.strftime("%H:%M:%S")

workout_info = {
    "tracker": {
        "date": formatted_now,
        "time": formatted_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

sheet_api = SheetyApi()

get_info = input("Would you like to print the latest workout info? y/n ").casefold()
if get_info == 'y':
    sheet_api.get_sheet_data()
post_new_day = input("Do you have add new workout data? y/n ").casefold()
if post_new_day == 'y':
    sheet_api.post_sheet_data(workout_info=workout_info)
else:
    print("No Data Stored.")
    exit(0)
