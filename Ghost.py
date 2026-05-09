
def prime_num(n) ->bool:
        if n <=1:
            return False
        elif n ==2:
            return True
        elif n % 2==0:
            return False
        # Fix: math is n**0.5 (square root), not 0.05
        # Loop over possible odd factors
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:  # Fix: checking n % i, not n % 2
                return False
        
        # If loop finishes and hasn't returned False, it means it's prime
        return True
while True:
    n = input('enter your number: ')
    if n =='stop':
        break
    num = int(n)
    print(prime_num(num))

from colorama import Fore,Style,init
init(autoreset=True)
n = 123
s = 0
while n > 0:
     d =n % 10
     s = s * 10 + d
     n = n//10
print(f'{Fore.CYAN} this is a Reversed number {Fore.GREEN} {s} {Fore.RESET}')




import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

def build_pipeline():
    # 1. Define feature types
    numeric_features = ['age', 'income', 'balance']
    categorical_features = ['city', 'occupation']

    # 2. Build Preprocessors
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # 3. Combine Preprocessors into a ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # 4. Attach the Model to the Pipeline
    full_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    return full_pipeline

def train_and_save_model(data_path, model_save_path):
    # Load data
    df = pd.read_csv(data_path)
    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build and Train Pipeline
    print("Building and training the pipeline...")
    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    # Evaluate
    print("Evaluating...")
    predictions = pipeline.predict(X_test)
    print(classification_report(y_test, predictions))

    # Save the entire pipeline (preprocessor + model)
    print(f"Saving model to {model_save_path}...")
    joblib.dump(pipeline, model_save_path)
    print("Done!")

# Example execution:
# train_and_save_model('dataset.csv', 'model.joblib')
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load the trained pipeline
model_pipeline = joblib.load("model.joblib")

# Define expected input schema
class InferenceRequest(BaseModel):
    age: float
    income: float
    balance: float
    city: str
    occupation: str

@app.post("/predict")
def predict(request: InferenceRequest):
    # Convert input to DataFrame (which the pipeline expects)
    input_data = pd.DataFrame([request.model_dump()])
    
    # The pipeline handles scaling and encoding automatically!
    prediction = model_pipeline.predict(input_data)
    
    return {"prediction": int(prediction[0])}
