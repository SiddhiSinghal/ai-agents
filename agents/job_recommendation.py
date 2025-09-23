import pickle, os, pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

def train_job_model(csv_file="Student Placement.csv"):
    df = pd.read_csv(csv_file)
    label_encoder = LabelEncoder()
    df['Profile'] = label_encoder.fit_transform(df['Profile'])

    X = df[['DSA','DBMS','OS','CN','Mathmetics','Aptitute','Comm','Problem Solving','Creative','Hackathons']]
    y = df['Profile']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    with open('job_model.pkl','wb') as f:
        pickle.dump(model,f)
    with open('label_encoder.pkl','wb') as f:
        pickle.dump(label_encoder,f)

def predict_jobs(user_data):
    with open('job_model.pkl','rb') as f:
        model = pickle.load(f)
    with open('label_encoder.pkl','rb') as f:
        le = pickle.load(f)

    if hasattr(model,'predict_proba'):
        probabilities = model.predict_proba([user_data])[0]
        top_3_indices = probabilities.argsort()[-3:][::-1]
        top_3_jobs = le.inverse_transform(top_3_indices).tolist()
    else:
        predicted_profile = model.predict([user_data])
        top_3_jobs = le.inverse_transform(predicted_profile).tolist()

    return top_3_jobs
