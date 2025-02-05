import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
import joblib

# Load dataset
file_path = "new.csv"  # Ensure this path is correct
df = pd.read_csv(file_path)

# Select features and target (only the 4 features the model needs)
X = df[['V1', 'V2', 'V3', 'V4']]  # Ensure consistency with prediction endpoint
y = df['Class']  # Target variable

# Normalize numerical values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Scale features

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# Apply SMOTE to balance classes
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Train model
model = RandomForestClassifier(n_estimators=10, max_depth=10, random_state=42, n_jobs=1)
model.fit(X_resampled, y_resampled)

# Save model
joblib.dump(model, "fraud_detection_model.joblib")
print("✅ Model training complete and saved!")
