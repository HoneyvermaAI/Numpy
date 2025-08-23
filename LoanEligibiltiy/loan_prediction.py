import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load Dataset
data = pd.read_csv("train.csv")
print("Original Data:\n", data.head())

# Step 2: Fill missing values
data.fillna(method='ffill', inplace=True)

# Step 3: Encode categorical features
le = LabelEncoder()
for column in data.columns:
    if data[column].dtype == 'object':
        data[column] = le.fit_transform(data[column])

# Step 4: Define input and output
X = data.drop(columns=['Loan_ID', 'Loan_Status'])  # Features
y = data['Loan_Status']                            # Target

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Step 6: Train Random Forest Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 7: Predictions
y_pred = model.predict(X_test)

# Step 8: Evaluation
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 9: Visualize Feature Importance
importances = model.feature_importances_
features = X.columns

plt.figure(figsize=(10, 6))
sns.barplot(x=importances, y=features)
plt.title("Feature Importance")
plt.tight_layout()
plt.show()

# Step 10: Test a new user's data (optional)
new_user = [[1, 0, 1, 0, 5849, 0, 128, 360, 1, 0, 1]]  # Example input
prediction = model.predict(new_user)
print("\nPrediction for new user (1 = Eligible, 0 = Not Eligible):", prediction)
