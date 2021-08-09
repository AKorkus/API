import json


class Meals:
    def __init__(self):
        try:
            with open("meals.json", "r") as f:
                self.meals = json.load(f)
        except FileNotFoundError:
            self.meals = []

    def all(self):
        return self.meals

    def get(self, id):
        meal = [meal for meal in self.all() if meal['id'] == id]
        if meal:
            return meal[0]
        return []

    def create(self, data):
        if "csrf_token" in data:
            data.pop("csrf_token")
        self.meals.append(data)
        self.save_all()

    def save_all(self):
        with open("meals.json", "w") as f:
            json.dump(self.meals, f)

    def update(self, id, data):
        meal = self.get(id)
        if "csrf_token" in data:
            data.pop("csrf_token")
        if meal:
            index = self.meals.index(meal)
            self.meals[index] = data
            self.save_all()
            return True
        return False

    def delete(self, id):
        meal = self.get(id)
        if meal:
            self.meals.remove(meal)
            self.save_all()
            return True
        return False


meals = Meals()
