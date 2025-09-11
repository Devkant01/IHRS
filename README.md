
# Intelligent Healthcare Recommendation System (IHRS)

IHRS is a web-based healthcare recommendation system that provides users with personalized, data-driven recommendations for doctors, moving beyond simple directory searches to an intelligent, explainable recommendation engine.

## Overview

The system empowers users to make informed healthcare decisions by leveraging a hybrid recommendation engine. It uses content-based filtering (matching symptoms, location, and preferences to doctor specialties) and, where possible, collaborative filtering (user ratings). The backend is powered by Python/Flask, and the frontend is a modern React app.

---

## Key Features

- **Personalized Search:** Users specify symptoms, location (auto-detected or manual), and doctor gender preference.
- **Content-Based Recommendations:** Matches user symptoms and preferences to doctor specialties, gender, and location.
- **Fallback Recommendations:** If a specialist is not available, the system suggests a General Medicine doctor with a helpful explanation.
- **Transparent Results:** Each recommendation includes a clear explanation of why it was suggested.
- **Modern, Responsive UI:** Built with React for a clean and interactive user experience.
- **Synthetic Data:** All doctor, user, and rating data is generated using realistic Indian names and districts from Andhra Pradesh and Bihar.

---

## Technology Stack

- **Backend:** Python, Flask, Pandas
- **Frontend:** React, HTML, CSS, JavaScript
- **Machine Learning:** Scikit-learn (for future collaborative filtering), Pandas
- **Data:** Synthetic CSVs generated with Pandas and Faker (customized for Indian context)

---

## How to Run This Project Locally

Follow these steps to run the project on your local machine:

### Prerequisites

- Python 3.8+
- Node.js and npm
- (Recommended) Python virtual environment tool (`venv`)

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/Your-Repo-Name.git
cd Your-Repo-Name
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt
python utils/data_generator.py  # Generates synthetic doctors, users, and ratings data
python app.py
```
*The backend server will start on `http://localhost:5000`.*

### 3. Frontend Setup

Open a **new terminal window** and run:

```bash
cd frontend
npm install
npm start
```
*The frontend application will open automatically in your browser at `http://localhost:5173`.*

---

## Ethical Considerations & Disclaimer

- **Privacy:** All user data in the synthetic dataset is anonymized and for demonstration only.
- **Disclaimer:** This application is a demonstration project and is **not a substitute for professional medical advice**. Always consult with a qualified healthcare provider for any medical concerns.