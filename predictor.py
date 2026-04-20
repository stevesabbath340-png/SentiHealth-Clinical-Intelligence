import pandas as pd
import sqlite3
from sklearn.tree import DecisionTreeRegressor
from logger import log_event

def run_ai_prediction():
    # Audit hook
    log_event("AI_Engine", "Predictive ML model executed on patient dataset.")
    
    print("\n--- AI RECOVERY PREDICTOR ---")
    
    try:
        conn = sqlite3.connect('sentihealth.db')
        df = pd.read_sql_query("SELECT Age, Condition, Recovery_Days FROM patients", conn)
        conn.close()

        # Prepare data (Basic One-Hot Encoding for the 'Condition' column)
        df_encoded = pd.get_dummies(df, columns=['Condition'])
        
        X = df_encoded.drop('Recovery_Days', axis=1) # Features
        y = df_encoded['Recovery_Days']              # Target

        # Train a simple model
        model = DecisionTreeRegressor()
        model.fit(X, y)

        # Make a dummy prediction for a 45-year-old with the first condition in the list
        sample_patient = X.iloc[[0]]
        prediction = model.predict(sample_patient)

        print(f"[+] AI Prediction Model Trained Successfully.")
        print(f"[+] Predicted Recovery Time for sample: {prediction[0]:.1f} days.")

    except Exception as e:
        print(f"[-] AI Error: {e}")
        log_event("Error", f"AI Prediction failed: {str(e)}")