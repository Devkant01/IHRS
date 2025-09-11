
from flask import Flask, request, jsonify
from models.content_based import get_content_based_recommendations
try:
    from models.collaborative import get_collaborative_recommendations
    collaborative_available = True
except ImportError:
    collaborative_available = False
from utils.location import detect_location

import os
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Ensure data files are loaded with absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
doctors_df = pd.read_csv(os.path.join(DATA_DIR, 'doctors.csv'))
users_df = pd.read_csv(os.path.join(DATA_DIR, 'users.csv'))
ratings_df = pd.read_csv(os.path.join(DATA_DIR, 'ratings.csv'))

@app.route('/location', methods=['GET'])
def location():
    user_location = detect_location(request)
    return jsonify({'location': user_location})

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_symptoms = data.get('symptoms', '')
    user_location = data.get('location', '')
    doctor_gender = data.get('doctor_gender', None)
    user_id = data.get('user_id', None)

    content_recs, content_explanations = get_content_based_recommendations(
        user_symptoms, user_location, doctor_gender, doctors_df
    )
    recommendations = content_recs
    explanations = content_explanations
    if collaborative_available and user_id is not None:
        collab_recs, collab_explanations = get_collaborative_recommendations(
            user_id, ratings_df, doctors_df
        )
        recommendations += [rec for rec in collab_recs if rec not in recommendations]
        explanations += collab_explanations
    elif not collaborative_available:
        explanations.append("Collaborative filtering is not available on this server.")
    return jsonify({'recommendations': recommendations, 'explanations': explanations})

if __name__ == '__main__':
    app.run(debug=True)
