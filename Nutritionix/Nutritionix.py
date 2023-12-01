import requests
from dataclasses import dataclass, field
from pprint import pp
try:
    from creds import NUTRITIONIX_ID, NUTRITIONIX_API_KEY
except ImportError:
    from .creds import NUTRITIONIX_ID, NUTRITIONIX_API_KEY


@dataclass
class NutritionixSetup:
    """
    :argument id: Nutritonix ID
    :argument api_key: Nutritonix API Key
    """
    id: str = field(compare=False)
    api_key: str
    user_info: dict = field(default_factory=dict)

    def post_nl_exercise(self, exercise: str) -> dict:
        """
            docs: https://developer.syndigo.com/docs/natural-language-for-exercise
        :param exercise: String of Exercise Completed.
                Example: 'ran 3 miles'
        :return: response.json
        """
        endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

        header = {
            "x-app-id": self.id,
            "x-app-key": self.api_key,
            "Content-Type": "application/json"
        }

        query = {
            'query': exercise,
        }

        if self.user_info:
            query.update(self.user_info)

        resp = requests.post(url=endpoint, json=query, headers=header)

        workout = resp.json()
        time_of_workout = workout['exercises'][0]['duration_min']
        calories_burned = workout['exercises'][0]['nf_calories']
        name_of_exercise = workout['exercises'][0]['name']
        # pp(workout)
        result = {
            "name": name_of_exercise,
            "calories_burned": calories_burned,
            "duration": time_of_workout
        }
        return result


if __name__ == "__main__":
    test_call = NutritionixSetup(id=NUTRITIONIX_ID, api_key=NUTRITIONIX_API_KEY)
    test_call.post_nl_exercise('ran 3 miles')
