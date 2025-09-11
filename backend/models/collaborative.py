from surprise import Dataset, Reader, SVD
import pandas as pd

def get_collaborative_recommendations(user_id, ratings_df, doctors_df):
    explanations = []
    if user_id is None or user_id not in ratings_df['user_id'].values:
        return [], []
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(ratings_df[['user_id', 'doctor_id', 'rating']], reader)
    trainset = data.build_full_trainset()
    algo = SVD()
    algo.fit(trainset)
    doctor_ids = doctors_df['doctor_id'].unique()
    predictions = [(doc_id, algo.predict(user_id, doc_id).est) for doc_id in doctor_ids]
    predictions.sort(key=lambda x: x[1], reverse=True)
    top_doctors = [doc_id for doc_id, _ in predictions[:5]]
    recommendations = doctors_df[doctors_df['doctor_id'].isin(top_doctors)].to_dict(orient='records')
    explanations = [f"Doctor {doc['name']} is highly rated by users like you." for doc in recommendations]
    return recommendations, explanations
