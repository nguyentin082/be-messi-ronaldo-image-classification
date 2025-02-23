import json
import joblib
import global_variables


def load_classification_model():

    print("Loading your model...............")

    with open('./class_dictionary.json', 'r') as f:
        global_variables.__dict = json.load(f)                                              # {'Messi': 0, 'Ronaldo': 1}
        global_variables. __number_to_name = list(global_variables.__dict.values())         # [0, 1]

    if global_variables.__model is None:
        with open('./saved_model.pkl', 'rb') as f:
            global_variables.__model = joblib.load(f)

    print("Done.")
