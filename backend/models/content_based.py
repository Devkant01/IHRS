import pandas as pd

def get_content_based_recommendations(symptoms, location, doctor_gender, doctors_df):
    # Simple content-based filtering: match symptoms to specialties, location, and gender
    filtered = doctors_df.copy()
    explanations = []
    if location:
        filtered = filtered[filtered['location'].str.contains(location, case=False, na=False)]
        explanations.append(f"Filtered by location: {location}")
    if doctor_gender:
        filtered = filtered[filtered['gender'].str.lower() == doctor_gender.lower()]
        explanations.append(f"Filtered by doctor gender: {doctor_gender}")
    if symptoms:
        filtered = filtered[filtered['specialties'].str.contains(symptoms, case=False, na=False)]
        explanations.append(f"Filtered by symptoms/specialty: {symptoms}")
    recommendations = filtered.head(5).to_dict(orient='records')
    explanations = [f"Doctor {doc['name']} matches your criteria." for doc in recommendations]

    # Fallback: if no specialized doctor found, recommend a General Medicine doctor with a helpful message
    if not recommendations:
        fallback = doctors_df.copy()
        if location:
            fallback = fallback[fallback['location'].str.contains(location, case=False, na=False)]
        if doctor_gender:
            fallback = fallback[fallback['gender'].str.lower() == doctor_gender.lower()]
        fallback = fallback[fallback['specialties'].str.lower() == 'general medicine']
        fallback_recs = fallback.head(1).to_dict(orient='records')
        if fallback_recs:
            recommendations = fallback_recs
            explanations = [
                f"Currently, a specialized doctor for '{symptoms}' is not available in your district, but Dr. {fallback_recs[0]['name']} (General Medicine) can help you with initial treatment and guidance."
            ]
    return recommendations, explanations
