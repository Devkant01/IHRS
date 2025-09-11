import pandas as pd
from faker import Faker
import random

fake = Faker()

specialties = [
    'Cardiology', 'Dermatology', 'Neurology', 'Pediatrics', 'General Medicine', 'Orthopedics',
    'Headache', 'Fever', 'Cough', 'Diabetes', 'Hypertension', 'Asthma', 'Allergy', 'Back Pain', 'Migraine'
]
ap_districts = [
    'Anantapur', 'Chittoor', 'East Godavari', 'Guntur', 'Krishna', 'Kurnool', 'Prakasam',
    'Nellore', 'Srikakulam', 'Visakhapatnam', 'Vizianagaram', 'West Godavari', 'Kadapa', 'Peddapuram'
]
bihar_districts = [
    'Araria', 'Arwal', 'Aurangabad', 'Banka', 'Begusarai', 'Bhagalpur', 'Bhojpur', 'Buxar',
    'Darbhanga', 'East Champaran', 'Gaya', 'Gopalganj', 'Jamui', 'Jehanabad', 'Kaimur', 'Katihar',
    'Khagaria', 'Kishanganj', 'Lakhisarai', 'Madhepura', 'Madhubani', 'Munger', 'Muzaffarpur',
    'Nalanda', 'Nawada', 'Patna', 'Purnia', 'Rohtas', 'Saharsa', 'Samastipur', 'Saran', 'Sheikhpura',
    'Sheohar', 'Sitamarhi', 'Siwan', 'Supaul', 'Vaishali', 'West Champaran'
]
locations = [d + ', Andhra Pradesh' for d in ap_districts] + [d + ', Bihar' for d in bihar_districts]

common_symptoms = [
    'Fever', 'Cough', 'Cold', 'Headache', 'Stomach Pain', 'Back Pain', 'Diabetes', 'Hypertension',
    'Asthma', 'Allergy', 'Migraine', 'Skin Rash', 'Chest Pain', 'Joint Pain', 'Infection', 'Weakness'
]
specialties = [
    'General Medicine', 'Pediatrics', 'Dermatology', 'Cardiology', 'Neurology', 'Orthopedics',
    'ENT', 'Pulmonology', 'Gastroenterology', 'Endocrinology', 'Psychiatry', 'Ophthalmology',
    'Dentistry', 'Gynecology', 'Urology', 'Nephrology', 'Oncology', 'Surgery'
] + common_symptoms
genders = ['Male', 'Female']

def generate_doctors():
    data = []
    indian_names = [
        'Dr. Rajesh Sharma', 'Dr. Priya Reddy', 'Dr. Anil Kumar', 'Dr. Sunita Singh',
        'Dr. Suresh Gupta', 'Dr. Meena Joshi', 'Dr. Amitabh Verma', 'Dr. Kavita Mishra',
        'Dr. Manoj Sinha', 'Dr. Neha Pandey', 'Dr. Rakesh Yadav', 'Dr. Swati Jha',
        'Dr. Sanjay Das', 'Dr. Pooja Agarwal', 'Dr. Ajay Kumar', 'Dr. Shalini Rao',
        'Dr. Deepak Singh', 'Dr. Ritu Sinha', 'Dr. Arvind Patel', 'Dr. Sneha Chatterjee',
        'Dr. Vikram Chauhan', 'Dr. Nisha Jain', 'Dr. Alok Tripathi', 'Dr. Ramesh Babu',
        'Dr. Vandana Iyer', 'Dr. Gaurav Saxena', 'Dr. Shweta Menon', 'Dr. Pradeep Joshi',
        'Dr. Anju Thomas', 'Dr. Sandeep Kaur', 'Dr. Manoj Pillai', 'Dr. Ruchi Sinha',
        'Dr. Ashok Mehta', 'Dr. Jyoti Rani', 'Dr. Kiran Desai', 'Dr. Pankaj Dubey',
        'Dr. Smita Kulkarni', 'Dr. Abhishek Singh', 'Dr. Radhika Nair', 'Dr. Mohan Rao',
        'Dr. Preeti Sharma', 'Dr. Yogesh Patil', 'Dr. Anil Sahu', 'Dr. Suman Mishra',
        'Dr. Rakesh Kumar', 'Dr. Nidhi Verma', 'Dr. Amit Sinha', 'Dr. Seema Gupta',
        'Dr. Dinesh Kumar', 'Dr. Pooja Singh'
    ]
    doc_id = 1
    name_idx = 0
    for loc in locations:
        for spec in specialties:
            name = indian_names[name_idx % len(indian_names)]
            gender = 'Male' if 'Dr. ' + name.split()[1] in ['Rajesh', 'Anil', 'Suresh', 'Amitabh', 'Manoj', 'Rakesh', 'Sanjay', 'Ajay', 'Deepak', 'Arvind', 'Vikram', 'Alok', 'Ramesh', 'Gaurav', 'Pradeep', 'Manoj', 'Ashok', 'Pankaj', 'Abhishek', 'Mohan', 'Yogesh', 'Anil', 'Dinesh'] else 'Female'
            data.append({
                'doctor_id': doc_id,
                'name': name,
                'gender': gender,
                'location': loc,
                'specialties': spec
            })
            doc_id += 1
            name_idx += 1
    # Add some default doctors for fallback
    for i in range(10):
        name = indian_names[(name_idx + i) % len(indian_names)]
        gender = 'Male' if 'Dr. ' + name.split()[1] in ['Rajesh', 'Anil', 'Suresh', 'Amitabh', 'Manoj', 'Rakesh', 'Sanjay', 'Ajay', 'Deepak', 'Arvind', 'Vikram', 'Alok', 'Ramesh', 'Gaurav', 'Pradeep', 'Manoj', 'Ashok', 'Pankaj', 'Abhishek', 'Mohan', 'Yogesh', 'Anil', 'Dinesh'] else 'Female'
        data.append({
            'doctor_id': doc_id,
            'name': name,
            'gender': gender,
            'location': random.choice(locations),
            'specialties': 'General Medicine'
        })
        doc_id += 1
    return pd.DataFrame(data)
def get_default_doctor_message(symptom):
    return f"Currently, a specialized doctor for '{symptom}' is not available in your district, but a General Medicine doctor can help you with initial treatment and guidance."

def generate_users(n=20):
    data = []
    for i in range(n):
        data.append({
            'user_id': i+1,
            'name': fake.name(),
            'location': random.choice(locations)
        })
    return pd.DataFrame(data)

def generate_ratings(users, doctors, n=200):
    data = []
    for _ in range(n):
        data.append({
            'user_id': random.choice(users['user_id']),
            'doctor_id': random.choice(doctors['doctor_id']),
            'rating': random.randint(1, 5)
        })
    return pd.DataFrame(data)

if __name__ == '__main__':
    import os
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    data_dir = os.path.abspath(data_dir)
    os.makedirs(data_dir, exist_ok=True)
    doctors = generate_doctors()
    users = generate_users()
    ratings = generate_ratings(users, doctors)
    doctors.to_csv(os.path.join(data_dir, 'doctors.csv'), index=False)
    users.to_csv(os.path.join(data_dir, 'users.csv'), index=False)
    ratings.to_csv(os.path.join(data_dir, 'ratings.csv'), index=False)
    print('Synthetic data generated.')
